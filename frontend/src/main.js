// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import 'core-js/es6/promise'
import 'core-js/es6/string'
import 'core-js/es7/array'
// import cssVars from 'css-vars-ponyfill'
import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import App from './App'
import router from './router'

import axios from 'axios'
import VueAxios from 'vue-axios'
import VueMoment from 'vue-moment'
import moment from 'moment-timezone'

switch (process.env.NODE_ENV) {
  case 'development':
    axios.defaults.baseURL = 'http://0.0.0.0:5000'
    break
  case 'production':
    axios.defaults.baseURL = ''
    break
  default:
    axios.defaults.baseURL = ''
    break
}

Vue.use(BootstrapVue)
Vue.use(VueAxios, axios)
Vue.use(VueMoment, {
  moment
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: {
    App
  }
})
