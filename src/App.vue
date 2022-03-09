<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo1.png">
    欢迎:{{msg}}
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue';
import Home from './components/Home.vue'
export default {
  name: 'App',
  data() {
    return {
      msg: 'wangziyuan',
    };
  },
  components: {
    HelloWorld,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
