<template>
    <li>{{ product.name }} - {{ product.price }}
      <button @click="InMyBag(product)">장바구니 추가</button>
    </li>
    
</template>


<script setup>

  const props = defineProps({
    product:Object
  })

  const emits = defineEmits(['InMyBag'])
  const InMyBag = () => {
    emits('InMyBag',product)
  }
</script>

<style scoped>

</style>