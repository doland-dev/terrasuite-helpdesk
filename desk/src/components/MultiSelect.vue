<template>
  <div class="flex flex-wrap gap-2 rounded-lg bg-gray-100 p-2">
    <Pill
      v-for="item in items"
      :key="item.value"
      :label="item.label"
      @click="(i) => remove(i)"
    />

    <Input
      v-model="input"
      class="w-full"
      :placeholder="placeholder"
      @keyup.enter="add({ label: input, value: input })"
    />
  </div>
</template>

<script setup lang="ts">
import { Input, toast } from "frappe-ui";
import { ref, toRefs } from "vue";
import Pill from "./Pill.vue";

type Item = {
  label: string;
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  value: any;
};

const props = defineProps({
  items: {
    type: Array<Item>,
    required: true,
  },
  placeholder: {
    type: String,
    required: false,
    default: "Type...",
  },
  validate: {
    type: Function,
    required: false,
    default: () => false,
  },
});

const emit = defineEmits<{
  (event: "update:items", items: Array<Item>): void;
}>();

const { items } = toRefs(props);
const input = ref("");

function add(item: Item) {
  const err = props.validate(item);

  if (err) {
    toast.error(err);

    return;
  }

  const res = [...items.value, item];
  emit("update:items", res);
  input.value = "";
}

function remove(item: Item) {
  const res = items.value.filter((i) => i.value !== item);
  emit("update:items", res);
}
</script>
