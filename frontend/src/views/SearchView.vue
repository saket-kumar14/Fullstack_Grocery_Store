<script setup>
import Search from '../components/Search.vue';
</script>

<template>
  <div class="search">
    <main>
      <Search/>
    </main>
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .register {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>