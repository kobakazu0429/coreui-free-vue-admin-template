<template>
  <div class="animated fadeIn">
    <b-col lg="12">
      <b-card header="Actions">
        <b-button variant="primary" @click="showModal('new-layer-modal')">新規作成</b-button>
        <b-modal :ref="'new-layer-modal'" size="lg" hide-footer hide-header>
          <div class="modal-body">
            <b-form-group>
              <label for="layer_name">レイヤー名</label>
              <b-form-input type="text" id="layer_name" v-model="layer_name"></b-form-input>
            </b-form-group>
            <b-form-group>
              <label for="layer_url">ソースURL</label>
              <b-form-input type="text" id="layer_url" v-model="layer_url"></b-form-input>
            </b-form-group>
            <b-form-group>
              <label for="layer_description">説明</label>
              <b-form-input type="text" id="layer_description" v-model="layer_description"></b-form-input>
            </b-form-group>
            <b-form-group>
              <label for="type">タイプ</label>
              <b-form-select id="type" :plain="false" :options="types" v-model="selected_type_id"></b-form-select>
            </b-form-group>
            <b-form-group>
              <label for="group">グループ</label>
              <b-form-select id="group" :plain="false" :options="groups" v-model="selected_group_id"></b-form-select>
            </b-form-group>
            <b-form-group>
              <label for="category">カテゴリー</label>
              <b-form-select id="category" :plain="false" :options="categories" v-model="selected_category_id"></b-form-select>
            </b-form-group>
            <b-form-group>
              <label for="format">フォーマット</label>
              <b-form-select id="format" :plain="false" :options="formats" v-model="selected_format_id"></b-form-select>
            </b-form-group>
            <b-form-group>
              <label for="attribute">出典</label>
              <b-form-select id="attribute" :plain="false" :options="attributes" v-model="selected_attribute_id"></b-form-select>
            </b-form-group>
          </div>
          <div class="modal-footer">
            <b-button variant="secondary" data-dismiss="modal" @click="hideModal('new-layer-modal')">キャンセル</b-button>
            <b-button variant="success" @click="postLayers">保存</b-button>
          </div>
        </b-modal>
      </b-card>
      <c-table bordered caption="Layers" :fields="fields" :items="items" :sort-by.sync="sortBy"></c-table>
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
  { key: 'attribute', label: '出典' },
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
      items: [],
      layer_name: '',
      layer_url: '',
      layer_description: '',
      types: [],
      groups: [],
      categories: [],
      formats: [],
      attributes: [],
      selected_type_id: null,
      selected_group_id: null,
      selected_category_id: null,
      selected_format_id: null,
      selected_attribute_id: null
    }
  },
  methods: {
    showModal(id) {
      this.$refs[id].show()
    },
    hideModal(id) {
      this.$refs[id].hide()
    },
    postLayers() {
      this.axios
        .post('/api/layers/', {
          type_id: this.selected_type_id,
          group_id: this.selected_group_id,
          category_id: this.selected_category_id,
          name: this.layer_name,
          url: this.layer_url,
          format_id: this.selected_format_id,
          attribute_id: this.selected_attribute_id,
          description: this.layer_description
        })
        .then(response => {
          location.reload()
        })
        .catch(error => {
          console.log(error)
        })
    },
    toSelectOptions(objs, key) {
      let tmp_arr = []
      for (let obj of objs) {
        let tmp_obj = {}
        tmp_obj.value = obj.id
        tmp_obj.text = key === 'attribute' ? `${obj['title']} - ${obj['url']}` : obj[key]
        tmp_arr.push(tmp_obj)
      }
      return tmp_arr
    }
  },
  mounted: function() {
    this.axios.get('/api/layers/').then(response => {
      this.items = response.data
    })
    this.axios.get('/api/types/').then(response => {
      this.types = this.toSelectOptions(response.data, 'type')
    })
    this.axios.get('/api/groups/').then(response => {
      this.groups = this.toSelectOptions(response.data, 'group')
    })
    this.axios.get('/api/categories/').then(response => {
      this.categories = this.toSelectOptions(response.data, 'category')
    })
    this.axios.get('/api/formats/').then(response => {
      this.formats = this.toSelectOptions(response.data, 'format')
    })
    this.axios.get('/api/attributes/').then(response => {
      this.attributes = this.toSelectOptions(response.data, 'attribute')
    })
  }
}
</script>
