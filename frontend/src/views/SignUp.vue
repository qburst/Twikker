<template>
    <div class="dark h-screen w-screen bg-gray-700 flex items-center justify-center">
        <div class="m-3 rounded-md border-2 border-gray-500">
            <div class="py-1 font-bold w-full border-b-2 border-gray-500">
                <div class="pl-2 py-1 font-bold w-full border-b-2 border-gray-500">
                    <h1 class="text-lg">Sign Up</h1>
                </div>
                <form @submit.prevent="submitForm" class="flex-col grid justify-items-end mb-2 p-3 font-medium">
                    <input type="text" name="username" v-model="username">
                    <input type="password" name="password" v-model="password">
                    <button type="submit" class="mt-3 px-2 border-2 bg-gray-100 hover:bg-gray-300 rounded-xl">Sign Up</button>
                </form>
            </div>
        </div>
    </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useRouter } from 'vue-router';

const router = useRouter();
 
const name = 'SignUp';
let username = ref('');
let password = ref('');

function submitForm(e){
    const formData = {
        username: username.value,
        password: password.value,
    }
    axios
        .post('api/v1/users/', formData)
        .then(response => {
            router.push('/login')
        })
        .catch(error => {
            console.log(error)
        })
}

</script>
