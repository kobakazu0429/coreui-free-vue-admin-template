<template>
  <b-card :header="caption">
    <b-form-group class="mb-3">
      <b-input-group>
        <b-form-input v-model="filter" placeholder="Type to Search" />
        <b-input-group-append>
          <b-btn :disabled="!filter" @click="filter = ''">Clear</b-btn>
        </b-input-group-append>
      </b-input-group>
    </b-form-group>
    <b-table :hover="hover" :striped="striped" :bordered="bordered" :small="small" :fixed="fixed" :fields="fields" :items="items" :sort-by.sync="sortBy" :sort-desc.sync="sortDesc" :filter="filter" @filtered="onFiltered" responsive="sm">
      <template slot="attribute" slot-scope="data">
        <a :href="data.item.attribute_utl">{{data.item.attribute_title}}</a>
      </template>
      <template slot="status" slot-scope="data">
      </template>
      <template slot="more-info" slot-scope="data">
        <b-btn @click="showModal('modal'+data.item.id)">詳細を開く</b-btn>
        <b-modal :ref="'modal'+data.item.id" title="詳細" hide-footer>
          <p>id : {{data.item.id}}</p>
          <p>name : {{data.item.name}}</p>
          <p>description : {{data.item.description}}</p>
          <p>url : {{data.item.url}}</p>
          <p>type : {{data.item.type}}</p>
          <p>group : {{data.item.group}}</p>
          <p>category : {{data.item.category}}</p>
          <p>format : {{data.item.format}}</p>
          <p>attribute_title : {{data.item.attribute_title}}</p>
          <p>attribute_utl : {{data.item.attribute_utl}}</p>
        </b-modal>
      </template>
      <template slot="updated_at_moment" slot-scope="data">
        <p>{{$moment(data.item.updated_at).tz('Etc/GMT').format('YYYY/MM/DD - HH:mm:ss')}}</p>
      </template>
      <template slot="created_at_moment" slot-scope="data">
        <p>{{$moment(data.item.created_at).tz('Etc/GMT').format('YYYY/MM/DD - HH:mm:ss')}}</p>
      </template>
      <template slot="actions" slot-scope="data">
        <b-button class="mr-3" variant="outline-primary" @click="showModal('edit-modal'+data.item.id)">編集</b-button>
        <b-button class="mr-3" variant="outline-danger" @click="$emit('delete-id', data.item.id)">削除</b-button>
        <b-modal :ref="'edit-modal'+data.item.id" title="編集" hide-footer>
          <div class="modal-body">
            <p>id : {{data.item.id}}</p>
            <b-form-group class="mb-3">
              <b-input-group>
                <b-form-input v-model="edited" :placeholder="'現在は「' + data.item.type + '」です'" />
                <b-input-group-append>
                  <b-btn :disabled="!edited" @click="edited = ''">Clear</b-btn>
                </b-input-group-append>
              </b-input-group>
            </b-form-group>
          </div>
          <div class="modal-footer">
            <b-button variant="secondary" data-dismiss="modal" @click="hideModal('edit-modal'+data.item.id)">キャンセル</b-button>
            <b-button variant="success" @click="$emit('edit-id', {id:data.item.id,edited:edited})">保存</b-button>
          </div>
        </b-modal>
      </template>
    </b-table>
  </b-card>
</template>

<script>
export default {
  name: 'c-table',
  data() {
    return {
      sortDesc: false,
      filter: null,
      edited: null
    }
  },
  methods: {
    getRowCount(items) {
      return items.length
    },
    onFiltered(filteredItems) {
      this.totalRows = filteredItems.length
      this.currentPage = 1
    },
    showModal(id) {
      this.$refs[id].show()
    },
    hideModal(id) {
      this.$refs[id].hide()
    }
  },
  props: {
    caption: {
      type: String,
      default: 'Table'
    },
    hover: {
      type: Boolean,
      default: false
    },
    striped: {
      type: Boolean,
      default: false
    },
    bordered: {
      type: Boolean,
      default: false
    },
    small: {
      type: Boolean,
      default: false
    },
    fixed: {
      type: Boolean,
      default: false
    },
    fields: {
      type: Array
    },
    items: {
      type: Array
    },
    sortBy: {
      type: String
    }
  }
}
</script>
