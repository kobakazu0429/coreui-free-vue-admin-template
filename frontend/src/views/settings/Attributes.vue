<template>
  <div class="animated fadeIn">
    <b-col lg="12">
      <b-card header="新規追加">
        <b-form inline onsubmit="return false;">
          <label class="mr-sm-2" for="inlineInput1">タイトル:</label>
          <b-input id="inlineInput1" class="mr-3 col-sm-2" type="text" placeholder="国土地理院「標準地図」" v-model="input_title"></b-input>
          <label class="mr-sm-2" for="inlineInput2">URL:</label>
          <b-input id="inlineInput2" class="mr-3 col-sm-4" type="text" placeholder="https://cyberjapandata.gsi.go.jp/xyz/std/{z}/{x}/{y}.png" v-model="input_url"></b-input>
          <b-button type="submit" size="sm" variant="primary" class="mr-3" @click="post">
            <i class="fa fa-dot-circle-o"></i>
            Submit
          </b-button>
          <b-button type="reset" size="sm" variant="danger" @click="input_title=''; input_url=''">
            <i class="fa fa-ban"></i>
            Reset
          </b-button>
        </b-form>
      </b-card>
      <c-table bordered caption="Attributes" :fields="fields" :items="items" :sort-by.sync="sortBy" @delete-id="delete_column" @edit-id="edit_column"></c-table>
    </b-col>
  </div>
</template>

<script>
import cTable from '../base/Table'

const fields = [
  { key: 'id', label: 'ID', sortable: true },
  { key: 'title', label: 'タイトル', sortable: true },
  { key: 'url', label: 'URL', sortable: true },
  { key: 'updated_at_moment', label: '更新日' },
  { key: 'created_at_moment', label: '作成日' },
  { key: 'actions', label: '操作' },
]

export default {
  name: 'attributes',
  components: {
    cTable,
  },
  data() {
    return {
      sortBy: 'id',
      fields: fields,
      items: null,
      input_title: null,
      input_url: null,
    }
  },
  mounted: function() {
    this.axios.get('/api/attributes/').then(response => {
      this.items = response.data
    })
  },
  methods: {
    post: function() {
      this.axios
        .post('/api/attributes/', {
          title: this.input_title,
          url: this.input_url,
        })
        .then(response => {
          location.reload()
        })
        .catch(error => {
          console.log(error)
        })
    },
    delete_column: function(id) {
      this.axios
        .delete(`/api/attributes/${id}/`)
        .then(response => {
          location.reload()
        })
        .catch(error => {
          console.log(error)
        })
    },
    edit_column: function(params) {
      this.axios
        .patch(`/api/attributes/${params.id}/`, {
          title: params.edited.title,
          url: params.edited.url,
        })
        .then(response => {
          location.reload()
        })
        .catch(error => {
          console.log(error)
        })
    },
  },
}
</script>
