<template>
    <div class="grid-container">
        <main>
            <!----------------->
            <!---- SEARCH ----->
            <!----------------->
            <section id="search" class="search-container">
                <h1 class="search-bar-title">درمانکده - مشاوره آنلاین و حضوری</h1>
                <div class="search-bar-container">
                    <input @input="searchDoctor" v-model="doctorName" type="text" class="search-input" placeholder="نام پزشک ، تخصص ، یا محله مورد نظر را جستجو کنید."/>
                    <div style="height: 100%;background-color: white;display: flex;justify-content: center;">
                        <i data-feather="map-pin" class="search-icon search-map-icon"></i>
                    </div>
                    <input type="text" readonly class="search-text-input text-steel" value="تهران" />
                    <div style="height: 100%;background-color: white;display: flex;justify-content: center;">
                        <i data-feather="chevron-down" class="search-icon"></i>
                    </div>
                    <button @click="searchFunc" class="default-button search-button">
                        جستجو
                    </button>
                </div>
                <div class="row justify-content-center mt-1">
                    <ul style="text-align: center;background-color: white;width: 50%">
                        <li v-for="doctor in doctors" :key="doctor.node.name">
                            <nuxt-link :to="'/doctor/'+doctor.node.pk">{{ doctor.node.name }}</nuxt-link>
                        </li>
                    </ul>
                </div>
            </section>
            <!----------------->
            <!-- SEARCH ENDS -->
            <!----------------->


            <!-------------------------->
            <!---- BEST PROFESSION ----->
            <!-------------------------->
            <section id="professions" class="best-professions-container">
                <div class="best-professions-header text-slate">
                    <div class="col-6">
                        <span class="right">بهترین تخصص های درمانکده</span>
                    </div>
                    <div class="col-6">
                        <span class="flex see-all left">
                            <nuxt-link to="/professions">
                                <span>مشاهده همه</span>
                                <i data-feather="chevron-left"></i>
                            </nuxt-link>
                        </span>
                    </div>
                </div>
                <div class="justified-flex best-profession-content">
                    <nuxt-link class="profession-item" v-for="profession in professions" :key="profession.title" :to="profession.link">
                        <div class="profession-image-holder" v-bind:style="{ 'background-color': profession.color}">
                            <img :src="profession.image"/>
                        </div>
                        <span>
                            {{ profession.title }}
                        </span>
                    </nuxt-link>
                </div>
            </section>
            <!-------------------------->
            <!-- BEST PROFESSION ENDS -->
            <!-------------------------->


            <!--------------------------->
            <!-------- COMMENTS --------->
            <!--------------------------->
            <section id="comments" class="comments-container">
                <div class="comments-description-container">
                    <div>
                        <h2 class="text-slate line-height-1-5">نظرات و روند درمانی بیماران</h2>
                        <p class="text-steel line-height-1-5">شما می توانید تجربه مراجعه کاربران دیگر به پزشکان را بخوانید و از علت مراجعه سایر بیماران و روند درمانی آن ها آگاهی یابید.</p>
                    </div>
                </div>
                <div class="comments-box-container">
                    <img src="images/comment.png" class="comment-image">
                    <div class="comments-area">
                        <div class="comments-comment text-slate">
                            <p>بسیار خوش برخورد و با اخلاق هستند و برای بیمار اهمیت زیادی رو قائل هستند.</p>
                        </div>
                        <div class="comments-comment-doctor-info">
                            <div class="comments-doctor-image">
                                <img src="images/doctor.jpg">
                                <div class="text-slate justified-flex">
                                    <p>
                                        <span style="font-weight: bold">دکتر محمود مطهری</span>
                                        <br />
                                        متخصص داخلی
                                    </p>
                                </div>
                            </div>
                            <div class="justified-flex-end mx-20" style="width: 50%">
                                <button class="default-button" style="font-size: 14px">
                                    مشاهده سایر نظرات
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            <!--------------------------->
            <!------ COMMENTS ENDS ------>
            <!--------------------------->


            <!--------------------------->
            <!---- SPECIAL SERVICES ----->
            <!--------------------------->
            <section id="services" class="speial-services-container">
                <h1>خدمات ویژه درمانکده برای مقابله با کرونا یا کووید-۱۹</h1>

                <div class="speial-services-content">
                    <div>
                        <img src="images/special-image-1.png" />
                        <h3>تست PCR و آنتی بادی در محل</h3>
                        <p style="text-align: right;">اگر در شهرهای تهران، مشهد، اصفهان، کرج، شیراز و اهواز هستید، می‌توانید بدون مراجعه به آزمایشگاه و در محل مدنظر خود آزمایش کرونا بدهید.</p>
                        <button class="justified-flex default-button">
                            <span>درخواست آزمایش</span>
                            <i data-feather="chevron-left"></i>
                        </button>
                    </div>
                    <div>
                        <img src="images/special-image-2.png" />
                        <h3>مشاوره آنلاین فوری</h3>
                        <p style="text-align: right;">با تست آنلاین کرونا علائم خود را بررسی کنید و اگر مشکوک بودید میتوانید به صورت فوری با پزشکان عمومی مشاوره آنلاین داشته باشید.</p>
                        <button class="justified-flex default-button">
                            <span>دریافت مشاوره فوری</span>
                            <i data-feather="chevron-left"></i>
                        </button>
                    </div>
                </div>
            </section>
            <!--------------------------->
            <!-- SPECIAL SERVICES ENDS -->
            <!--------------------------->


            <!------------------->
            <!---- DOWNLOAD ----->
            <!------------------->
            <section id="download" class="download-container justified-flex">
                <div class="download-block">
                    <img src="images/download.png" />
                    <div>
                        <a href="#"><img src="images/play-store.png" /></a>
                        <a href="#"><img src="images/app-store.png" /></a>
                        <a href="#"><img src="images/bazar.png" /></a>
                    </div>
                </div>
                <div class="download-block align-right text-slate">
                    <br />
                    <h2 class="download-header-text">دانلود اپلیکیشن درمانکده</h2>
                    <p class="download-text text-steel">با اپلیکیشن درمانکده با پزشکان و روانشناسان آنلاین مشاوره کنید یا برای ویزیت حضوری آنلاین نوبت بگیرید.</p>
                    <h3 class="download-header-text" style="font-size: 1rem;">برای دریافت لینک دانلود، شماره موبایل خود را وارد کنید.</h3>
                    <div class="flex" style="justify-content: flex-start !important;">
                        <input type="text" class="download-mobile-input" placeholder="مانند  ******* 0912  " >
                        <div class="download-button-container">
                            <button class="download-button">
                                <i data-feather="smartphone" class="download-phone-icon"></i>
                                <span>ارسال لینک</span>
                            </button>
                            <div class="download-button-overlay"></div>
                        </div>
                        
                    </div>
                </div>
            </section>
            <!------------------->
            <!-- DOWNLOAD ENDS -->
            <!------------------->
        </main>
        <footer>
            <div class="footer-top">
                <img src="images/login-logo.svg" />
                <p>درمانکده، ارائه دهنده خدمات آنلاین سلامت</p>
                <p>(نوبت گیری اینترنتی، مشاوره آنلاین، آزمایش در محل و ...)</p>
            </div>
            <div class="footer-middle">
                <div id="footer-middle-right">
                    <ul class="centered-ul">
                        <li><a>درباره درمانکده</a></li>
                        <li><a>تماس با ما</a></li>
                        <li><a>مجله پزشکی</a></li>
                    </ul>
                </div>
                <div id="footer-middle-center">
                    <div class="footer-social-media-container">
                        <i data-feather="instagram"></i>
                        <i data-feather="twitter"></i>
                        <i data-feather="linkedin"></i>
                    </div>
                    <div id="middle-line">

                    </div>
                </div>
                <div id="footer-middle-left">
                    <ul class="centered-ul">
                        <li><a>سوالات متداول</a></li>
                        <li><a>قوانین سایت</a></li>
                        <li><a>شکایت</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>با ثبت‌نام در خبرنامه درمانکده، اولین نفری باشید که از جدیدترین خبرها، جشنواره‌ها و تخفیف های ویژه ما مطلع می‌شوید</p>
                <div class="subscribe-form">
                    <input id="first-name" type="text" placeholder="نام" />
                    <input id="last-name" type="text" placeholder="نام خانوادگی" />
                    <input id="email" type="email" placeholder="ایمیل" />
                    <div id="submit" class="download-button-container">
                        <button class="download-button">
                            <i data-feather="arrow-left" class="download-phone-icon"></i>
                            <span style="width: 85%">عضو میشوم</span>
                        </button>
                        <div class="download-button-overlay"></div>
                    </div>
                </div>
                <div class="authorities">
                    <img src="images/sabt.png">
                    <img src="images/etemad.png">
                </div>
            </div>
            <div class="footer-copyright text-slate">
                <p id="copyright">تمامی حقوق این سایت برای فراهانی محفوظ است</p>
                <p id="author">تولید شده توسط تیم درمانکده</p>
            </div>
        </footer>
    </div>
</template>

<script>
export default {
    data(){
        return {
            professions: [
                {title: 'ارتوپدی', image: 'images/1.png', link: '/doctors', color: '#e8c9fd'},
                {title: 'اورولوژی', image: 'images/2.png', link: '/doctors', color: '#fcbaba'},
                {title: 'پوست و مو', image: 'images/3.png', link: '/doctors', color: '#b3e8ca'},
                {title: 'زنان و زایمان', image: 'images/4.png', link: '/doctors', color: '#abc2d8'},
                {title: 'داخلی', image: 'images/5.png', link: '/doctors', color: '#fbcbee'},
                {title: 'گوش، حلق و بینی', image: 'images/6.png', link: '/doctors', color: '#c5e1fb'},
                {title: 'مغز و اعصاب', image: 'images/7.png', link: '/doctors', color: '#fdcdb0'},
            ],
            doctorName: "",
            doctors: null,
            interval: null
        }
    },
    head() {
        title: "درمانکده"
    },
    methods: {
        searchDoctor: function(){
            if(!this.doctorName){
                this.doctors = null
                return
            }
            console.log("salam")
            this.$apollo.query({
                query: require('../graphql/doctors.gql'),
                variables: {
                    name: this.doctorName
                }
            }).then(data => {
                console.log(data.data.doctors.edges)
                this.doctors = data.data.doctors.edges
            }).catch(error => {
                console.log(error)
            })
        },
        searchFunc: function(){
            this.$router.push('/doctors?name='+this.doctorName)
        }
    }
}
</script>

<style scoped>
@import url('@/assets/index.css');
</style>