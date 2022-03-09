<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo1.png"> -->
  </div>
</template>

<script>
import Home from './components/Home.vue'
export default {
  name: 'App',
  components: {
    Home,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  margin-left: auto;
  margin-right: auto;
  max-width: 980px;
  color: #2c3e50;
}
</style>
