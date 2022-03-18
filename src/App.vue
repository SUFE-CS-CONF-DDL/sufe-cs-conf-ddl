<template>
  <div id="app">
<!--    <img alt="SIME AILAB logo" src="ai-lab-logo.png" class="top_logo">-->
    <Home></Home>
  </div>
</template>

<script>
import Home from './components/Home.vue';

export default {
  name: 'App',
  components: {
    Home,
  },
};
</script>

<style>
#app {
  font-family: "Roboto","Helvetica Neue",Helvetica,Arial,sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  margin-left: auto;
  margin-right: auto;
  max-width: 980px;
  /*color: #2c3e50;*/

/* 设置logo格式 */

}
.top_logo {
  margin-right: 1.3%;
}
</style>
