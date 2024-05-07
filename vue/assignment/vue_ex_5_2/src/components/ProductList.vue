<template>
  <ul>
    <ProductListItem 
      v-for="product in products"
      :key="product.id"
      :product="product"
      @InMyBag="InMyBag"
    />
  </ul>
</template>

<script setup>
import ProductListItem from '@/components/ProductListItem.vue'
const props = defineProps({
  products: Array
})

const emits = defineEmits(['InMyBag'])
const InMyBag = function(product) {
  emits('InMyBag',product)
}
</script>
