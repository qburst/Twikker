<template>
    <div id="conversationapp" class="flex flex-col h-full max-[600px]:mb-14">
        <div id="chatcontainer" class="flex flex-col h-full mx-3 mt-2">
            <div class="mb-1.5" v-for="message in messages" :class="message.tweeker_name == userStore.username ? 'justify-end flex w-full' : 'flex w-full' ">
                <article class="flex h-fit w-fit max-w-md p-2 pt-3 pl-3 border-solid border-2 border-gray-200 dark:border-gray-700 bg-lchat shadow-md dark:bg-gray-700" :class="message.tweeker_name == userStore.username ? 'rounded-tl-3xl rounded-tr-3xl  rounded-bl-3xl' : 'rounded-tl-3xl rounded-tr-3xl  rounded-br-3xl' ">
                    <figure class="shrink-0">
                        <Avatar />
                    </figure>
                    <div class="flex-col ml-2.5">
                        <div>
                            <strong>
                                <a  href="">{{ message.tweeker_name }}</a>
                            </strong>
                            <small>{{ message.formatted_time }}</small>
                        </div>
                        <div class="break-all">
                            <span>{{ message.content }}</span>
                        </div>
                    </div>
                </article>
            </div>
        </div>
        <div class="p-2 sticky flex bg-white dark:bg-dark bottom-0  max-[600px]:bottom-14 w-full items-center">
                <div class="w-full">
                    <form class="m-0" v-on:submit.prevent="submitMessage()">
                        <input v-model="content" type="text" class="rounded-xl px-2 h-10 w-full text-base outline-none text-black dark:text-white bg-lchat dark:bg-gray-700" placeholder="Your message...">
                    </form>
                </div>
                <div class="bg-lchat dark:bg-gray-700 hover:bg-gray-500 ml-1 rounded-xl">
                    <button @click="submitMessage()" class="h-10 w-10 text-green-300 px-2 rounded-full hover:text-green-500"><i class="fa-regular fa-paper-plane"></i></button>
                </div>
        </div>
    </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted, computed } from 'vue'
import { useUserStore } from '../store/UserStore.js'
import Avatar from './Avatar.vue'
const userStore = useUserStore();


const props = defineProps(['user_id']);



let conversation_id = '0';
const messages = ref([]);
const content = ref('');
const tweeker = computed(() => userStore.username);
const formatted_time = 'Now';
const avatar = '';
let chatSocket = null;
const current_room = 'global';

async function getConversationId(){
    await axios.get(`/api/get_conversation/${props.user_id}`)
    .then(response => {
        conversation_id = response.data.conversation_id;
    })
    .catch(error => {
    })
}
async function getMessages(){
    if (props.user_id){
        await getConversationId();
    }
    await axios.get(`/api/messages/${conversation_id}`,) 
    .then(response => {
        for (let i = 0; i < response.data.messages.length; i++) {
            messages.value.push(response.data.messages[i])
        }
    }).then(() => {
        setTimeout(() => {
            scrollToBottom();
        }, 0);
    })
    .catch(error => {
        console.log('error 1' + error)
    })
}
function submitMessage() {
    if (content.value.length > 0) {
        let message = {
            'content': content.value,
            'tweeker_name': tweeker.value,
            'formatted_time': formatted_time,
            'avatar_url': avatar,
            'conversation_id': conversation_id,
        };
        chatSocket.send(JSON.stringify(message));
        content.value = '';
    }
}
function scrollToBottom() {
    window.scrollTo(0, document.body.scrollHeight);
}
onMounted(() => {
    getMessages();
    var loc = window.location, new_uri;
    if (loc.protocol === "https:") {
        new_uri = "wss:";
    } else {
        new_uri = "ws:";
    }
    new_uri += "//" + import.meta.env.VITE_SOCKET_HOST;
    chatSocket = new WebSocket(
        new_uri +
        '/ws/' +
        'chat/' +
        conversation_id +
        '/'
    );
    //append to messages when receive message
    chatSocket.onmessage = function (e) {
        const data = JSON.parse(e.data);
        // append message to messages
        messages.value.push(data);
        setTimeout(() => {
            scrollToBottom();
        }, 0);
    }.bind(this);
})
</script>