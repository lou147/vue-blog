<template>
  
    <div id="main">

        <div style="text-align: center;margin-top: 50px;" class="animated fadeIn">
          <div class="view-num" style="margin-bottom: 30px ">
            <div style="font-size: 22px">访问次数：{{view_num}}</div>
            <div style="font-size: 22px">访问人数：{{view_people}} </div>
          </div>

          <p>Leo</p>


          <div style="margin-top: 30px">
            <a id="about-icon" href="http://www.jianshu.com/u/c4adda69f8eb"><i class="iconfont icon-jian"></i></a>
            <a id="about-icon" href="http://weibo.com/5180092490/profile?rightmod=1&wvr=6&mod=personnumber&is_all=1"><i class="iconfont icon-weibo"></i></a>
            <a id="about-icon" href="https://github.com/lou147"><i class="iconfont icon-github"></i></a>
            <a id="about-icon" @click="showQQSwitch"><i class="iconfont icon-3"><span v-show="showQQ" style="font-size: 13px">: 778617402</span></i></a>
          </div>
        </div>
        
    </div>

</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      showQQ: false,
      view_num:'',
      view_people:''
    }
  },
  created(){
    document.title = 'About',
    this.about(),
    this.getView()
  },
  methods:{
    about:function() {
      this.$emit('about')
    },
    showQQSwitch:function() {
      this.showQQ = !this.showQQ
    },
    getView:function(){
      var self = this;
      axios.get('/api/view_num/').then(function(response){
        console.log(response);
        self.view_num = response.data.view_num;
        self.view_people = response.data.view_people
      })
    }
  }

}
</script>


