<template>
    <div class="flex flex-col w-full border-solid border-x-2 border-gray-100 dark:border-gray-700 max-[600px]:border-x-0">
        <div class="min-[600px]:sticky p-3 bg-white dark:bg-dark top-0 w-full h-fit min-[600px]:opacity-90 text-2xl border-b-2 border-gray-700 ">
            <a href="{% url 'global' %}">
                <span class="opacity-100 font-semibold">Conversation</span>
            </a>
        </div>
        <div class="flex flex-col h-full w-full">
            <ChatBox :user_id="id"></ChatBox>
        </div>
    </div>
</template>

<script setup>
import ChatBox from '../components/ChatBox.vue';

const props = defineProps(['id']);

</script>
