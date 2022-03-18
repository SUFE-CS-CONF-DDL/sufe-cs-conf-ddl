import Vue from 'vue/dist/vue';
import ElementUI from 'element-ui';

import 'element-ui/lib/theme-chalk/index.css';

import VueResource from 'vue-resource';

import VueCountdown from '@chenfengyuan/vue-countdown';

import Storage from 'vue-ls';

import App from './App.vue';

Vue.use(ElementUI);
Vue.use(VueResource);
Vue.component(VueCountdown.name, VueCountdown);

const options = {
  namespace: 'vuejs__',
  name: 'ls',
  storage: 'local',
};
Vue.use(Storage, options);
Vue.config.productionTip = false;

new Vue({
  render: (h) => h(App),
}).$mount('#app');
