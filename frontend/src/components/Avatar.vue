<template>
    <div class="flex shrink-0 w-12 h-full mr-1">
        <img
        class="rounded-full h-12 w-12"
        :src="img"
        />
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';
import { useUserStore } from '../store/UserStore.js'

const userStore = useUserStore();

const img = ref('https://res.cloudinary.com/deues3qyn/image/upload/v1676499936/avatar.png');

async function getProfileData(tweeker_username) {
  await axios
    .get(`/api/profile_data/${tweeker_username}`)
    .then((response) => {
      return response.data["profile"];
    })
    .catch((error) => {
      console.log("error" + error);
    });
}

onMounted(() => {
    getProfileData(userStore.username);    
});
</script>