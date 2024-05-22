<template>
  <h2 style="color: black;">현재 상영중인 영화</h2>
  <div class="user-ranking">
    <table class="ranking-table">
      <tbody>
        <tr v-for="movie in movies" :key="movie.rank">
          <td>{{ movie.rank }}</td>
          <td>{{ movie.movieNm }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { onMounted, ref } from 'vue'
import axios from 'axios';

export default {
  setup() {
    const movies = ref([]);
    const API_KEY = import.meta.env.VITE_KOFIC_API_KEY
    onMounted(() => {
      const dt = new Date();
      const m = dt.getMonth() + 1 < 10 ? '0' + (dt.getMonth() + 1) : dt.getMonth() + 1
      const d = dt.getDate() - 1 < 10 ? '0' + (dt.getDate() - 1) : dt.getDate() - 1
      const y = dt.getFullYear()
      const result = y + m + d
      console.log(result)
      axios({
        method: 'get',
        url: `http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?key=${API_KEY}&targetDt=${result}&itemPerPage=5`
      })
        .then(response => {
          const parser = new DOMParser()
          const xmlDoc = parser.parseFromString(response.data, 'text/xml')
          const dailyBoxOfficeList = xmlDoc.getElementsByTagName('dailyBoxOffice')
          for (let i = 0; i < dailyBoxOfficeList.length; i++) {
            const movie = {
              rank: dailyBoxOfficeList[i].getElementsByTagName('rank')[0].childNodes[0].nodeValue,
              movieNm: dailyBoxOfficeList[i].getElementsByTagName('movieNm')[0].childNodes[0].nodeValue,
              openDt: dailyBoxOfficeList[i].getElementsByTagName('openDt')[0].childNodes[0].nodeValue,
              audiAcc: dailyBoxOfficeList[i].getElementsByTagName('audiAcc')[0].childNodes[0].nodeValue
            }
            movies.value.push(movie)
          }
        })
        .catch(error => console.log(error))
    });

    // 3자리씩 끊어서 출력하는 함수
    function formatAudiAcc(acc) {
      const regex = /\B(?=(\d{3})+(?!\d))/g;
      return acc.toString().replace(regex, ",");
    }

    return {
      movies,
      formatAudiAcc
    };
  }
}
</script>

<style scoped>
.user-ranking {
  max-width: 800px;
  /* 전체적으로 크기를 키웁니다 */
  margin: 0 auto;
}

.ranking-table {
  width: 100%;
  border-collapse: collapse;
}

.ranking-table td {
  padding: 12px;
  /* 셀 내부 여백을 늘립니다 */
  text-align: left;
}

.ranking-table tbody tr:nth-child(even) {
  background-color: #f9f9f9;
}

.ranking-table tbody {
  background-color: #f2f2f2;
}


</style>