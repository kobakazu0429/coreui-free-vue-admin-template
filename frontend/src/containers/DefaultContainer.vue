<template>
  <div class="app">
    <AppHeader fixed>
      <SidebarToggler />
      <b-link class="navbar-brand" to="#">
        <img class="navbar-brand-full" src="img/brand/logo.svg" width="89" height="25" alt="CoreUI Logo">
        <img class="navbar-brand-minimized" src="img/brand/sygnet.svg" width="30" height="30" alt="CoreUI Logo">
      </b-link>
    </AppHeader>
    <div class="app-body">
      <AppSidebar fixed>
        <SidebarNav :navItems="nav"></SidebarNav>
        <SidebarFooter/>
      </AppSidebar>
      <main class="main">
        <Breadcrumb :list="list"/>
        <div class="container-fluid">
          <router-view></router-view>
        </div>
      </main>
    </div>
    <TheFooter fixed>
      &copy; 2018 - by&nbsp;<a href="https://github.com/kobakazu0429/">@kobakazu0429.</a>
    </TheFooter>
  </div>
</template>

<script>
import nav from '@/_nav'
import {
  Header as AppHeader,
  SidebarToggler,
  Sidebar as AppSidebar,
  SidebarFooter,
  SidebarNav,
  Breadcrumb,
  Footer as TheFooter
} from '@coreui/vue'

export default {
  name: 'full',
  components: {
    AppHeader,
    AppSidebar,
    TheFooter,
    Breadcrumb,
    SidebarFooter,
    SidebarToggler,
    SidebarNav
  },
  data() {
    return {
      nav: nav.items
    }
  },
  computed: {
    name() {
      return this.$route.name
    },
    list() {
      return this.$route.matched.filter(route => route.name || route.meta.label)
    }
  }
}
</script>
