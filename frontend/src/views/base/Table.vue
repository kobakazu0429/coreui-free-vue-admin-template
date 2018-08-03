<template>
  <b-card :header="caption">
    <!-- filer -->
    <b-form-group class="mb-3">
      <b-input-group>
        <b-form-input v-model="filter" placeholder="Type to Search" />
        <b-input-group-append>
          <b-btn :disabled="!filter" @click="filter = ''">Clear</b-btn>
        </b-input-group-append>
      </b-input-group>
    </b-form-group>

    <!-- table -->
    <b-table :hover="hover" :striped="striped" :bordered="bordered" :small="small" :fixed="fixed" :fields="fields" :items="items" :sort-by.sync="sortBy" :sort-desc.sync="sortDesc" :filter="filter" responsive="sm">

      <!-- 出典カラム:リンクで飛べるようにする -->
      <template slot="attribute" slot-scope="data">
        <a :href="data.item.attribute_utl">{{data.item.attribute_title}}</a>
      </template>

      <!-- ステータスカラム -->
      <template slot="status" slot-scope="data"></template>

      <!-- 更新日カラム -->
      <template slot="updated_at_moment" slot-scope="data">
        <p>{{$moment(data.item.updated_at).tz('Etc/GMT').format('YYYY/MM/DD - HH:mm:ss')}}</p>
      </template>

      <!-- 作成日カラム -->
      <template slot="created_at_moment" slot-scope="data">
        <p>{{$moment(data.item.created_at).tz('Etc/GMT').format('YYYY/MM/DD - HH:mm:ss')}}</p>
      </template>

      <!-- 操作カラム -->
      <template slot="actions" slot-scope="data">
        <!-- layersの時は詳細ボタンの表示 -->
        <template v-if="data.item.name !== undefined">
          <b-button class="mr-1" variant="outline-dark" @click="showModal('modal'+data.item.id)">詳細</b-button>
        </template>

        <b-button class="mr-1" variant="outline-primary" @click="showModal('edit-modal'+data.item.id)">編集</b-button>
        <b-button variant="outline-danger" @click="$emit('delete-id', data.item.id)">削除</b-button>

        <!-- 詳細モーダル -->
        <template v-if="data.item.name !== undefined">
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

        <!-- 編集モーダル -->
        <b-modal :ref="'edit-modal'+data.item.id" title="編集" size="lg" hide-footer>
          <div class="modal-body">
            <p>id : {{data.item.id}}</p>

            <!-- Layers.vue用 -->
            <template v-if="data.item.name !== undefined">
              <b-form-group>
                <label for="layer_name">レイヤー名</label>
                <b-form-input class="mb-1" v-model="edited.name" :placeholder="`現在は「${data.item.name}」です`" />
              </b-form-group>
              <b-form-group>
                <label for="layer_url">ソースURL</label>
                <b-form-input class="mb-1" v-model="edited.url" :placeholder="`現在は「${data.item.url}」です`" />
              </b-form-group>
              <b-form-group>
                <label for="layer_description">説明</label>
                <b-form-input class="mb-1" v-model="edited.description" :placeholder="`現在は「${data.item.description}」です`" />
              </b-form-group>
              <b-form-group>
                <label for="type">{{`タイプ: 現在は「${data.item.type}」です`}}</label>
                <b-form-select class="mb-1" :plain="false" :options="selectData.types" v-model="edited.type_id"></b-form-select>
              </b-form-group>
              <b-form-group>
                <label for="group">{{`グループ: 現在は「${data.item.group}」です`}}</label>
                <b-form-select class="mb-1" :plain="false" :options="selectData.groups" v-model="edited.group_id"></b-form-select>
              </b-form-group>
              <b-form-group>
                <label for="category">{{`カテゴリー: 現在は「${data.item.category}」です`}}</label>
                <b-form-select class="mb-1" :plain="false" :options="selectData.categories" v-model="edited.category_id"></b-form-select>
              </b-form-group>
              <b-form-group>
                <label for="format">{{`フォーマット: 現在は「${data.item.format}」です`}}</label>
                <b-form-select class="mb-1" :plain="false" :options="selectData.formats" v-model="edited.format_id"></b-form-select>
              </b-form-group>
              <b-form-group>
                <label for="attribute">{{`出典: 現在は「${data.item.attribute_title} - ${data.item.attribute_utl}」です`}}</label>
                <b-form-select class="mb-1" :plain="false" :options="selectData.attributes" v-model="edited.attribute_id"></b-form-select>
              </b-form-group>
            </template>

            <b-form-group class="mb-3" v-if="data.item.name === undefined">
              <b-input-group>
                <!-- Types.vue用 -->
                <template v-if="data.item.type !== undefined && data.item.name === undefined">
                  <b-form-input v-model="edited.type" :placeholder="`現在は「${data.item.type}」です`" />
                </template>

                <!-- Groups.vue用 -->
                <template v-if="data.item.group !== undefined && data.item.name === undefined">
                  <b-form-input v-model="edited.group" :placeholder="`現在は「${data.item.group}」です`" />
                </template>

                <!-- Categories.vue用 -->
                <template v-if="data.item.category !== undefined && data.item.name === undefined">
                  <b-form-input v-model="edited.category" :placeholder="`現在は「${data.item.category}」です`" />
                </template>

                <!-- Formats.vue用 -->
                <template v-if="data.item.format !== undefined && data.item.name === undefined">
                  <b-form-input v-model="edited.format" :placeholder="`現在は「${data.item.format}」です`" />
                </template>

                <!-- Attributes.vue用 -->
                <template v-if="data.item.attribute_title !== undefined && data.item.name === undefined">
                  <b-form-input v-model="edited.title" :placeholder="`現在は「${data.item.attribute_title}」です`" />
                  <b-form-input v-model="edited.url" :placeholder="`現在は「${data.item.attribute_utl}」です`" />
                </template>

                <b-input-group-append>
                  <b-btn :disabled="!edited" @click="edited = {}">Clear</b-btn>
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
      edited: null,
      edited: {
        name: null,
        url: null,
        description: null,
        type_id: null,
        group_id: null,
        category_id: null,
        format_id: null,
        attribute_id: null,
      },
    }
  },
  methods: {
    showModal(id) {
      this.$refs[id].show()
    },
    hideModal(id) {
      this.$refs[id].hide()
    },
  },
  props: {
    caption: {
      type: String,
      default: 'Table',
    },
    hover: {
      type: Boolean,
      default: false,
    },
    striped: {
      type: Boolean,
      default: false,
    },
    bordered: {
      type: Boolean,
      default: false,
    },
    small: {
      type: Boolean,
      default: false,
    },
    fixed: {
      type: Boolean,
      default: false,
    },
    fields: {
      type: Array,
    },
    items: {
      type: Array,
    },
    sortBy: {
      type: String,
    },
    selectData: {
      type: Object,
    },
  },
}
</script>
