export default {
  items: [
    {
      title: true,
      name: 'General',
      class: '',
      wrapper: {
        element: '',
        attributes: {}
      }
    },
    {
      name: 'Layers',
      url: '/layers',
      icon: 'icon-layers'
    },
    {
      title: true,
      name: 'Settings',
      class: '',
      wrapper: {
        element: '',
        attributes: {}
      }
    },
    {
      name: 'Types',
      url: '/settings/types',
      icon: 'icon-settings'
    },
    {
      name: 'Groups',
      url: '/settings/groups',
      icon: 'icon-settings'
    },
    {
      name: 'Categories',
      url: '/settings/categories',
      icon: 'icon-settings'
    },
    {
      name: 'Formats',
      url: '/settings/formats',
      icon: 'icon-settings'
    },
    {
      name: 'Attributes',
      url: '/settings/attributes',
      icon: 'icon-settings'
    },
    // add -------------------------------------------------------
    {
      title: true,
      name: 'Theme',
      class: '',
      wrapper: {
        element: '',
        attributes: {}
      }
    },
    {
      name: 'Colors',
      url: '/theme/colors',
      icon: 'icon-drop'
    },
    {
      title: true,
      name: 'Components',
      class: '',
      wrapper: {
        element: '',
        attributes: {}
      }
    },
    {
      name: 'Base',
      url: '/base',
      icon: 'icon-puzzle',
      children: [
        {
          name: 'Forms',
          url: '/base/forms',
          icon: 'icon-puzzle'
        },
        {
          name: 'Paginations',
          url: '/base/paginations',
          icon: 'icon-puzzle'
        },
        {
          name: 'Progress Bars',
          url: '/base/progress-bars',
          icon: 'icon-puzzle'
        },
        {
          name: 'Switches',
          url: '/base/switches',
          icon: 'icon-puzzle'
        },
        {
          name: 'Tabs',
          url: '/base/tabs',
          icon: 'icon-puzzle'
        }
      ]
    },
    {
      name: 'Buttons',
      url: '/buttons',
      icon: 'icon-cursor',
      children: [
        {
          name: 'Buttons',
          url: '/buttons/standard-buttons',
          icon: 'icon-cursor'
        },
        {
          name: 'Button Dropdowns',
          url: '/buttons/dropdowns',
          icon: 'icon-cursor'
        },
        {
          name: 'Button Groups',
          url: '/buttons/button-groups',
          icon: 'icon-cursor'
        }
      ]
    },
    {
      name: 'Icons',
      url: '/icons',
      icon: 'icon-star',
      children: [
        {
          name: 'CoreUI Icons',
          url: '/icons/coreui-icons',
          icon: 'icon-star',
          badge: {
            variant: 'info',
            text: 'NEW'
          }
        },
        {
          name: 'Font Awesome',
          url: '/icons/font-awesome',
          icon: 'icon-star',
          badge: {
            variant: 'secondary',
            text: '4.7'
          }
        },
        {
          name: 'Simple Line Icons',
          url: '/icons/simple-line-icons',
          icon: 'icon-star'
        }
      ]
    },
    {
      name: 'Notifications',
      url: '/notifications',
      icon: 'icon-bell',
      children: [
        {
          name: 'Badges',
          url: '/notifications/badges',
          icon: 'icon-bell'
        },
        {
          name: 'Modals',
          url: '/notifications/modals',
          icon: 'icon-bell'
        }
      ]
    },
    {
      name: 'Widgets',
      url: '/widgets',
      icon: 'icon-calculator'
    },
    {
      divider: true
    },
    {
      title: true,
      name: 'Extras'
    },
    {
      name: '呉高専マップ',
      url: 'https://kure-kosen-map.netlify.com/map.html',
      icon: 'icon-map'
    }
  ]
}
