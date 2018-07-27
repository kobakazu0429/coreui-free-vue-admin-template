<template>
  <div class="animated fadeIn">
      <b-col lg="12">
        <c-table
          bordered
          caption="Layers"
          :fields="fields"
          :items="items"
          :sort-by.sync="sortBy"
        ></c-table>
      </b-col>
  </div>
</template>




<script>
import cTable from './base/Table'

const fields = [
  { key: 'id', label: 'ID', sortable: true },
  { key: 'name', label: 'レイヤー名', sortable: true },
  { key: 'type', label: 'タイプ', sortable: true },
  { key: 'group', label: 'グループ', sortable: true },
  { key: 'category', label: 'カテゴリー', sortable: true },
  { key: 'format', label: 'フォーマット', sortable: true },
  { key: 'attribute', label: '出典', sortable: true },
  { key: 'status', label: 'ステータス', sortable: true },
  { key: 'more-info', label: '詳細' }
]

export default {
  name: 'layers',
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
    this.axios.get('http://0.0.0.0:5000/api/layers/').then(response => {
      this.items = response.data
    })
  }
}
</script>
