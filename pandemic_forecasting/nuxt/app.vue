<script setup lang="ts">
const { data, error } = await useFetch('http://fastapi:8000/')
</script>

<template>
  <div>
    <pre>{{ data }}</pre>
  </div>
</template>