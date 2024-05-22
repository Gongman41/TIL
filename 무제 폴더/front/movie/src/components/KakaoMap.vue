<template>
  <!-- <div class="kakao-map-wrapper">
    <iframe id="kakao-map-iframe" src="https://map.kakao.com/?q=영화관"
      style="width: 200px; height: 200px; border: none;"></iframe>
  </div> -->

  <div class="kakao-map-wrapper">
    <iframe id="kakao-map-iframe"
      src="https://m.map.kakao.com/actions/searchView?q=%EC%98%81%ED%99%94%EA%B4%80&wxEnc=YQRONOHR&wyEnc=LSWMTRHR&lvl=4#!/all/map/place"></iframe>
  </div>
</template>

<script>
export default {
  name: 'KakaoMapIframe',
};
</script>

<style scoped>
/* Optional: Add some styles to ensure the iframe takes up the full viewport height */
html,
body,
#app {
  margin: 0;
  padding: 0;
  height: 100%;
}

.kakao-map-wrapper {
  width: 200px;
  height: 200px;
}

#kakao-map-iframe {
  width: 300px;
  height: 300px;
  border: none;
}
</style>
