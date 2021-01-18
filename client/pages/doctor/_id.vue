<template>
    <main v-if="doctor" class="container mb-5 px-0">
        <div class="row mb-4">
            <nav class="nav">
              <nuxt-link class="nav-link px-0 d-flex align-items-center active" to="/">درمانکده <i data-feather="chevron-left"></i></nuxt-link>
                <nuxt-link class="nav-link px-0 d-flex align-items-center active" :to="'/doctors?spec='+doctor.spec.id" tabindex="-1" aria-disabled="true">{{ doctor.spec.name }}<i data-feather="chevron-left"></i></nuxt-link>
              <a class="nav-link px-0 disabled" href="#" tabindex="-1" aria-disabled="true">{{ doctor.name }}</a>
            </nav>
        </div>

        <!-- ******* -->
        <!-- DOCTOR -->
        <!-- ******* -->

        <div class="row" style="line-height: 26px">

            <!-- sticky sidebar -->
            <div class="col-md-4 pl-5 pr-0">
                <div class="row p-3 mb-4 justify-content-center sticky-top" style="background-color: #1780df;border-radius: 10px">
                    <div class="col-md-12" style="color: white">
                        <div class="row justify-content-center mb-2">
                            <i data-feather="heart" class="my-icon favorite-icon" style="position: absolute;top: 20px;left: 20px;color: white"></i>
                            <i data-feather="share-2" class="my-icon" style="position: absolute;top: 20px;right: 20px;color: white"></i>
                            <img style="border-radius: 100%;width: 50%" :src="doctor.avatar">
                        </div>
                        <div class="text-center">
                            <h5>{{ doctor.name }}</h5>
                            <p class="font-14 m-0">{{ doctor.spec.name }}</p>
                            <p class="font-14">شماره نظام پزشکی: {{ doctor.number }}</p>
                        </div>
                        <div class="row text-steel p-2" style="border-radius: 10px;background-color: white;">
                            <div class="col-md-4 text-center">
                                <i data-feather="book" class=""></i>
                                <p class="m-0 font-12">تجربه</p>
                                <h6 class="m-0 font-14 font-weight-bold">{{ doctor.experienceYears }} سال</h6>
                            </div>
                            <div class="col-md-4 text-center">
                                <i data-feather="clock"></i>
                                <p class="m-0 font-12">اولین نوبت آزاد</p>
                                <h6 class="m-0 font-14 font-weight-bold">{{ doctor.first_empty_date }}</h6>
                            </div>
                            <div class="col-md-4 text-center">
                                <i data-feather="credit-card"></i>
                                <p class="m-0 font-12">پرداخت آنلاین</p>
                                <h6 class="m-0 font-14 font-weight-bold">{{ onlinePay }}</h6>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- sticky sidebar -->

            <div class="col-md-8 px-0 pb-3 doctor-items-container">


                <!-- ************* -->
                <!-- Date and Time -->
                <!-- ************* -->
                <div class="card my-card mb-3">
                    <div class="card-header my-card-header" style="border-radius: 10px 10px 0 0">
                        <button class="p-2 font-weight-bold" style="background-color: #1780df;color: white;border-radius: 5px">
                            مطب چهارراه پونک
                        </button>
                    </div>
                    <div class="card-body">
                        <div class="row justify-content-center align-items-center">
                            <i data-feather="chevron-right" class="p-1" style="width: 36px;height: 36px;border-radius: 100%;border: 1px solid #fb815e;color: #fb815e"></i>
                            <div class="col-md-10 d-flex justify-content-around">
                                <div class="card mx-2 p-2 container-fluid text-center text-ocean">
                                    <h5 class="font-14 mb-1 font-weight-bold">امروز</h5>
                                    <h4 class="font-weight-bold m-0">۲۴</h4>
                                    <p class="font-12 m-0">آذر</p>
                                </div>
                                <div class="card mx-2 p-2 container-fluid text-center text-ocean">
                                    <h5 class="font-14 mb-1 font-weight-bold">امروز</h5>
                                    <h4 class="font-weight-bold m-0">۲۴</h4>
                                    <p class="font-12 m-0">آذر</p>
                                </div>
                                <div class="card mx-2 p-2 container-fluid text-center text-ocean">
                                    <h5 class="font-14 mb-1 font-weight-bold">امروز</h5>
                                    <h4 class="font-weight-bold m-0">۲۴</h4>
                                    <p class="font-12 m-0">آذر</p>
                                </div>
                                <div class="card mx-2 p-2 container-fluid text-center date-disabled">
                                    <h5 class="font-14 mb-1 font-weight-bold">امروز</h5>
                                    <h4 class="font-weight-bold m-0">۲۴</h4>
                                    <p class="font-12 m-0">آذر</p>
                                </div>
                                <div class="card mx-2 p-2 container-fluid text-center date-disabled">
                                    <h5 class="font-14 mb-1 font-weight-bold">امروز</h5>
                                    <h4 class="font-weight-bold m-0">۲۴</h4>
                                    <p class="font-12 m-0">آذر</p>
                                </div>
                                <div class="card mx-2 p-2 container-fluid text-center date-disabled">
                                    <h5 class="font-14 mb-1 font-weight-bold">امروز</h5>
                                    <h4 class="font-weight-bold m-0">۲۴</h4>
                                    <p class="font-12 m-0">آذر</p>
                                </div>
                            </div>
                            <i data-feather="chevron-left" class="p-1" style="width: 36px;height: 36px;border-radius: 100%;border: 1px solid #fb815e;color: #fb815e"></i>
                        </div>
                        <div class="card my-card my-3 p-3">
                            <div class="d-flex text-steel">
                                <i data-feather="clock"></i>
                                <p class="m-0 pr-2">ساعت های نوبت یکشنبه ۱ دی</p>
                            </div>
                            <div class="d-flex">
                                <button class="date-disabled my-3 ml-5 py-2 px-3 rounded border">
                                    <h5 class="m-0"><strong><strike>۱۷:۳۰</strike></strong></h5>
                                </button>
                                <button class="my-button my-3 ml-5 py-2 px-3 rounded border reserve-button">
                                    <h5 class="m-0 container-fluid"><strong></strong></h5>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- ************* -->
                <!-- Date and Time -->
                <!-- ************* -->


                <!-- *********** -->
                <!-- INFORMATION -->
                <!-- *********** -->
                <div class="card my-3" style="border-radius: 10px">
                    <div class="card-header p-0 d-flex border-0" style="background-color: #ededed">
                        <div class="d-flex p-3 justify-content-center align-items-center text-steel" @click="activeTab=true" style="border-radius: 0 10px 0 0" :class="{'active-tab text-ocean': activeTab}">
                            <i data-feather="map" class="ml-2"></i>
                            <p class="m-0">اطلاعات مطب</p>
                        </div>
                        <div class="d-flex p-3 justify-content-center align-items-center text-steel" @click="activeTab=false" :class="{'active-tab text-ocean': !activeTab}">
                            <i data-feather="calendar" class="ml-2"></i>
                            <p class="m-0">روزهای حضور</p>
                        </div>
                    </div>
                    <div v-if="activeTab" class="card-body row">
                        <div class="col-md-5 pl-5">
                            <img src="https://www.darmankade.com/Content/UploadFiles/LocationMedicalCenters/134image.png" style="width: 100%;border-radius: 10px">
                        </div>
                        <div class="col-md-7">
                            <p class="text-slate font-weight-bold">آدرس مطب ۱:</p>
                            <p class="text-slate">{{ doctor.address }}</p>
                            <p class="text-slate"><strong>تلفن گویا: </strong>{{ doctor.phone }}</p>
                        </div>
                    </div>
                    <div v-else class="card-body row justify-content-around rounded">
                        <div class="card border-0 p-2 text-steel text-center" v-for="(day, index) in days" :key="day" style="background-color: #fafafa">
                            {{ day }}
                            <div v-html="checkSVG" style="color:#4dcc6b" class="p-3" v-if="doctor.weekDays[index]"></div>
                            <div v-html="timesSVG" style="color:#fb815e" class="p-3" v-else></div>
                        </div>
                    </div>
                </div>
                <!-- *********** -->
                <!-- INFORMATION -->
                <!-- *********** -->


                <!-- ******* -->
                <!-- COMMENT -->
                <!-- ******* -->
                <div class="card my-3 border-radius-10">
                    <div class="card-header" style="background-color: #ededed">
                        <div class="row container-fluid text-slate">
                            <i data-feather="message-square" class="ml-3"></i>
                            <p class="m-0 font-weight-bold text-18">نظرات کاربران (تعداد کل نظرات :{{doctor.comments.length}})</p>
                        </div>
                        <div class="row container-fluid">
                            <i data-feather="message-square" class="ml-3 invisible"></i>
                            <p class="m-0 text-steel font-14">در این قسمت شما می توانید تجربه مراجعه کاربران دیگر به مطب آقای دکتر مهران جلالی را بخوانید.</p>
                        </div>
                    </div>
                    <div class="card-body">
                        <div class="row">
                            <div class="col-md-6">
                            <div class="row container text-slate">
                                <i data-feather="star" class="ml-2"></i>
                                <p class="font-weight-bold">امتیاز به پزشک</p>
                            </div>
                            <div class="row container align-items-center text-steel">
                                <p class="m-0">۵ ستاره</p>
                                <div style="width: 60%;height: 5px;border-radius: 20px;background-color: #fafafa" class="mx-2">
                                    <div style="width: 86%;height: 5px;border-radius: 20px;background-color: #1780df"></div>
                                </div>
                                <p class="m-0">43</p>
                            </div>
                            <div class="row container align-items-center text-steel">
                                <p class="m-0">۴ ستاره</p>
                                <div style="width: 60%;height: 5px;border-radius: 20px;background-color: #fafafa" class="mx-2">
                                    <div style="width: 12%;height: 5px;border-radius: 20px;background-color: #1780df"></div>
                                </div>
                                <p class="m-0">6</p>
                            </div>
                            <div class="row container align-items-center text-steel">
                                <p class="m-0">۳ ستاره</p>
                                <div style="width: 60%;height: 5px;border-radius: 20px;background-color: #fafafa" class="mx-2">
                                    <div style="width: 4%;height: 5px;border-radius: 20px;background-color: #1780df"></div>
                                </div>
                                <p class="m-0">2</p>
                            </div>
                            <div class="row container align-items-center text-steel">
                                <p class="m-0">۲ ستاره</p>
                                <div style="width: 60%;height: 5px;border-radius: 20px;background-color: #fafafa" class="mx-2">
                                    <div style="width: 0;height: 5px;border-radius: 20px;background-color: #1780df"></div>
                                </div>
                                <p class="m-0">0</p>
                            </div>
                            <div class="row container align-items-center text-steel">
                                <p class="m-0">۱ ستاره</p>
                                <div style="width: 60%;height: 5px;border-radius: 20px;background-color: #fafafa" class="mx-2">
                                    <div style="width: 2%;height: 5px;border-radius: 20px;background-color: #1780df"></div>
                                </div>
                                <p class="m-0">1</p>
                            </div>
                        </div>
                            <div class="col-md-6">
                                <div class="row container text-slate">
                                    <i data-feather="watch" class="ml-2"></i>
                                    <p class="font-weight-bold">میانگین زمان انتظار برای ویزیت</p>
                                </div>
                                <div class="row container text-slate">
                                    <i data-feather="watch" class="ml-2 invisible"></i>
                                    <p class="font-14">۴۵ دقیقه</p>
                                </div>
                            </div>
                        </div>
                        <div class="row mt-4">
                            <div class="card container my-card">
                                <div class="row  p-3">
                                    <i data-feather="align-right" class="ml-2"></i>
                                    <div class="text-slate">
                                        <strong>مرتب سازی براساس:</strong>
                                    </div>
                                    <div class="col-md-6">
                                        <div class="row justify-content-around">
                                            <div class="text-steel">
                                                جدیدترین
                                            </div>
                                            <div class="text-steel">
                                                بیشترین امتیاز
                                            </div>
                                            <div style="color: white;background-color: #1780df;border-radius: 10px" class="px-2 py-1">
                                                مفیدترین نظرات
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div v-for="comment in doctor.comments" :key="comment.title" class="card container mt-4 border-radius-10">
                                <div class="card-header row align-items-center">
                                    <i data-feather="user" class="text-slate ml-3"></i>
                                    <p class="text-steel m-0 font-14">نظر {{comment.author.name}} در تاریخ {{comment.createdAt}}</p>
                                    <div style="color: #4dcc6b;position: absolute;left: 5px">
                                        <i data-feather="thumbs-up" style="width: 18px"></i>
                                        <p class="mb-0 font-12" style="margin-top: -15px">11</p>
                                    </div>
                                </div>
                                <div class="card-body row">
                                    <div class="col-md-2">
                                        <p class="font-weight-bold text-slate">علت مراجعه به پزشک</p>
                                    </div>
                                    <div class="col-md-2">
                                        <div class="row">
                                            <p class="text-steel">{{ comment.title }}</p>
                                        </div>
                                        <div class="row justify-content-around">
                                            <i data-feather="star" v-for="i in comment.rate" :key="i" class="text-ocean" style="fill: #1780df;width: 16px"></i>
                                        </div>
                                    </div>
                                    <div class="col-md-8 pr-5">
                                        <p class="text-slate">{{ comment.text }}</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- ******* -->
                <!-- COMMENT -->
                <!-- ******* -->

                <div class="card my-3 border-radius-10">
                    <div class="card-header" style="background-color: #ededed">
                       ثبت نظر
                    </div>
                    <div class="card-body">
                        <input type="text" style="border: 2px solid black;width: 50%" class="my-1" v-model="comment.title" placeholder="عنوان" />
                        <br />
                        <textarea style="border: 2px solid black;width: 50%" v-model="comment.text" placeholder="متن" />
                        <br />
                        <input type="number" style="border: 2px solid black;width: 50%" class="my-1" v-model="comment.rate" min="0" max="5" placeholder="امتیاز" />
                        <br />
                        <button @click="issueComment" class="btn btn-primary">ثبت</button>
                    </div>
                </div>

            </div>
        </div>

        <!-- ******* -->
        <!-- DOCTOR -->
        <!-- ******* -->


    </main>
</template>

<script>
import feather from 'feather-icons'

export default {
    layout: 'pages',
    data() {
        return {
            doctor: null,
            activeTab: true,
            days: [
                'شنبه',
                'یکشنبه',
                'دوشنبه',
                'سه شنبه',
                'چهارشنبه',
                'پنج شنبه',
                'جمعه',
            ],
            comment: {
                title: "",
                text: "",
                rate: null,
                doctor: null
            }
        }
    },
    created: async function(){
        await this.init()
        this.$nextTick(() => {
            feather.replace()
        })
    },
    methods: {
        init: async function(){
            await this.$apollo.query({
                query: require('../../graphql/doctors.gql'),
                variables: {
                    pk: this.$route.params.id
                }
            }).then(data => {
                this.doctor = data.data.doctors.edges[0].node
                this.comment.doctor = this.doctor.pk
                console.log(this.doctor)
            }).catch(error => {
                console.log(error)
            })
        },
        issueComment: function(){
            this.$apollo.mutate({
                mutation: require('../../graphql/commentMutation.gql'),
                variables: {
                    input: this.comment
                }
            }).then(data => {
                console.log()
                this.doctor.comments.push(data.data.commentMutation)
                this.comment = {
                    title: "",
                    text: "",
                    rate: null,
                    doctor: this.doctor.pk
                }
            }).catch(error => {
                console.log(error)
            })
        }
    },
    computed: {
        onlinePay: function(){
            return this.doctor.onlinePay?'دارد':'ندارد'
        },
        checkSVG: function(){
            return feather.toSvg('check')
        },
        timesSVG: function(){
            return feather.toSvg('x')
        }
    }
}
</script>

<style scoped>
    @import url('@/assets/doctor.css');
    .active-tab {
        background-color: white;
    }
</style>