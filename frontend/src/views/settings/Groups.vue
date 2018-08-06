<template>
  <div class="animated fadeIn">
    <b-col lg="12">
      <b-card header="新規追加">
        <b-form inline onsubmit="return false;">
          <label class="mr-sm-2" for="inlineInput1">グループ:</label>
          <b-input id="inlineInput1" class="mr-3" type="text" placeholder="国土地理院" v-model="input"></b-input>
          <b-button type="submit" size="sm" variant="primary" class="mr-3" @click="post">
            <i class="fa fa-dot-circle-o"></i>
            Submit
          </b-button>
          <b-button type="reset" size="sm" variant="danger" @click="input=''">
            <i class="fa fa-ban"></i>
            Reset
          </b-button>
        </b-form>
      </b-card>
      <c-table bordered caption="Groups" :fields="fields" :items="items" :sort-by.sync="sortBy" @delete-id="delete_column" @edit-id="edit_column"></c-table>
    </b-col>
  </div>
</template>

<script>
import cTable from '../base/Table'

const fields = [
  { key: 'id', label: 'ID', sortable: true },
  { key: 'group', label: 'グループ', sortable: true },
  { key: 'updated_at_moment', label: '更新日' },
  { key: 'created_at_moment', label: '作成日' },
  { key: 'actions', label: '操作' },
]

export default {
  name: 'group',
  components: {
    cTable,
  },
  data() {
    return {
      sortBy: 'id',
      fields: fields,
      items: null,
      input: null,
    }
  },
  mounted: function() {
    this.axios.get('/api/groups/').then(response => {
      this.items = response.data
    })
  },
  methods: {
    post: function() {
      this.axios
        .post('/api/groups/', {
          group: this.input,
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
        .delete(`/api/groups/${id}/`)
        .then(response => {
          location.reload()
        })
        .catch(error => {
          console.log(error)
        })
    },
    edit_column: function(params) {
      this.axios
        .patch(`/api/groups/${params.id}/`, {
          group: params.edited.group,
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
