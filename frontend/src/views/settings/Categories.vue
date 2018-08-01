<template>
  <div class="animated fadeIn">
    <b-col lg="12">
      <c-table bordered caption="Categories" :fields="fields" :items="items" :sort-by.sync="sortBy"></c-table>
    </b-col>
  </div>
</template>

<script>
import cTable from '../base/Table'

const fields = [
  { key: 'id', label: 'ID', sortable: true },
  { key: 'category', label: 'カテゴリー', sortable: true },
  { key: 'updated_at_moment', label: '作成日' },
  { key: 'created_at_moment', label: '更新日' }
]

export default {
  name: 'categories',
  components: {
    cTable
  },
  data() {
    return {
      sortBy: 'id',
      fields: fields,
      items: null
    }
  },
  mounted: function() {
    this.axios.get('/api/categories/').then(response => {
      this.items = response.data
    })
  }
}
</script>
