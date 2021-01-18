<template>
    <main class="container mb-5">
        <div class="row mb-5">
            <img src="images/professions/slider.png" style="width: 100%">
        </div>
        <div class="row" style="line-height: 26px">
            <div class="col col-md-3 pl-3 pr-0">
                <div class="card sticky-top">
                    <div class="card-header px-1 py-3 d-flex justify-content-around align-items-center">
                        <i data-feather="align-right"></i>
                        <span>
                            <strong>همه تخصص ها</strong>
                            <span class="text-steel" style="font-size: 12px">
                                (به ترتیب حروف الفبا)
                            </span>
                        </span>
                    </div>
                    <div class="card-body">
                        <div class="row align-items-center px-1 py-2 search-container">
                            <i data-feather="search" class="search-icon"></i>
                            <input type="text" class="search-input" placeholder="تخصص مورد نظر خود را جستجو کنید..." />
                        </div>
                        <div class="row justify-content-start mx-0 my-4 alphabet-list-container">
                            <div class="col col-md-12 px-0 professions-list text-steel">
                                <div class="row px-2 mb-2">
                                    <div class="alphabet">ا</div>
                                </div>
                                <p>ارتوپدی</p>
                                <p>ارتوپدی کودکان</p>
                                <p>ارتوز و پروتز(ارتوپدی فنی)</p>
                                <p>استروتاکسی و فانکشنال مغز و اعصاب</p>
                                <p>آسم آلرژی و ایمونولوژی</p>
                                <p>اکوکاردیوگرافی</p>
                                <p>اندرولوژی و لاپاراسکوپی</p>
                                <p>اندویورولوژی و لاپاراسکوپی</p>
                                <p>آنژیوپلاستی</p>
                                <p>آنستزیولوژی-کنترل و درمان دردهای حاد و مزمن</p>
                                <p>آنکولوژی زنان</p>
                                <p>اورولوژی کودکان</p>
                                <p>اینترونشن نرواسکولار</p>
                                <p>اینترونشنال الکتروفیزیولوژی و پیس میکر</p>
                                <p>اینترونشنال کاردیولوژی</p>
                                <div class="row px-2 mb-2">
                                    <div class="alphabet">ب</div>
                                </div>
                                <p>بالون آنژیوپلاستی</p>
                                <p>بالون آنژیوپلاستی و والوپلاستی</p>
                                <p>بیماری های عفونی و تب دار</p>
                                <p>بیماریهای پوست و مو</p>
                                <p>بیماریهای ریه</p>
                                <p>بیماریهای عفونی کودکان</p>
                                <p>بیماریهای قلب و عروق</p>
                                <p>بیهوشی</p>
                                <div class="row px-2 mb-2">
                                    <div class="alphabet">پ</div>
                                </div>
                                <p>پوست و مو</p>
                                <p>پیوند کلیه</p>
                                <div class="row px-2 mb-2">
                                    <div class="alphabet">ت</div>
                                </div>
                                <p>تعویض مفاصل و آرتروسکوپی</p>
                                <p>تغذیه</p>
                                <p>توانبخشی شناختی</p>
                                <p>توراکس</p>
                                <div class="row px-2 mb-2">
                                    <div class="alphabet">ج</div>
                                </div>
                                <p>جراح کلیه و مجاری ادراری(اورولوژی)</p>
                                <p>جراحی بیماری های مادرزادی قلب</p>
                                <p>جراحی بینی و سینوس (رینولوژی)</p>
                                <p>جراحی پستان</p>
                                <p>جراحی پلاستیک و زیبایی</p>
                                <p>جراحی دست</p>
                                <p>جراحی زانو</p>
                                <p>جراحی ستون فقرات</p>
                                <p>جراحی سر و گردن</p>
                                <p>جراحی شانه</p>
                                <p>جراحی شبکیه و لیزر</p>
                                <p>جراحی عمومی</p>
                                <p>جراحی فک و صورت</p>
                                <p>جراحی قلب و عروق</p>
                                <p>جراحی کولورکتال</p>
                                <p>جراحی گلوکوم</p>
                                <p>جراحی لاپاروسکوپی</p>
                                <p>جراحی مغز و اعصاب</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col col-md-9 pb-3 profession-items-container" style="height: 100vh;overflow: scroll;overflow-x: hidden">
                <div class="row text-slate">
                    <nuxt-link v-for="spec in specs" :key="spec.id" :to="'/doctors?spec='+spec.id" style="text-decoration: none" class="col col-md-4 pl-0 pr-3 text-slate">
                        <div class="card p-3 profession-item-card">
                            <div class="row align-items-center justify-content-start px-3">
                                <img class="ml-2" src="images/professions/1.svg">
                                <h5>{{ spec.name }}</h5>
                            </div>
                            <div class="row text-steel px-3 my-4 font-14">
                                <p>متخصص گوارش، کبد و آندوسکوپی پزشکی که بر سلامت گوارش تمرکز دارد و در زمینه تشخیص، ارزیابی و درمان اختلالا ...</p>
                            </div>
                            <div class="row">
                                <div class="col-md-6 sina text-center">
                                    <img style="margin-left: -10px" src="https://www.darmankade.com/UploadFiles/Doctor/131900292329095031%D8%B7%D8%A7%D9%87%D8%B1%D9%87-%D9%85%D8%AD%D9%85%D9%88%D8%AF%D8%B2%D8%A7%D8%AF%D9%87.jpg" alt="طاهره محمودزاده" class="dr-img rounded-circle" data-v-35f6788e="">
                                    <img style="margin-left: -10px" src="https://www.darmankade.com/UploadFiles/Doctor/131899666226532118%D8%AF%DA%A9%D8%AA%D8%B1-%D9%85%D8%B9%D8%B5%D9%88%D9%85%D9%87-%D9%85%DB%8C%D8%B1%D8%A7%D8%B3%D9%85%D8%A7%D8%B9%DB%8C%D9%84%DB%8C.jpg" alt="معصومه میراسماعیلی" class="dr-img rounded-circle absolute-img1" data-v-35f6788e="">
                                    <img src="https://www.darmankade.com/UploadFiles/Doctor/131899428764941709%D8%AF%DA%A9%D8%AA%D8%B1-%D9%85%D9%87%D8%B1%D8%A7%D9%86%D8%AF%D8%AE%D8%AA-%D8%B9%D8%A7%D8%A8%D8%AF%DB%8C%D9%86%DB%8C.jpg" alt="مهراندخت عابدینی" class="dr-img rounded-circle absolute-img2" data-v-35f6788e="">
                                    <p class="mt-1 mb-0 text-center font-weight-bold font-12">
                                        + 14 پزشک
                                    </p>
                                </div>
                                <div class="col-md-6">
                                    <button class="default-button d-flex justify-content-center align-items-center">مشاهده<i style="width: 20px" data-feather="arrow-left"></i></button>
                                </div>
                            </div>
                        </div>
                    </nuxt-link>
                </div>
            </div>
        </div>
    </main>
</template>

<script>
export default {
    layout: 'pages',
    data() {
        return {
            specs: []
        }
    },
    created: function(){
        this.$apollo.query({
            query: require('../graphql/specs.gql')
        }).then(data => {
            console.log(data.data)
            this.specs = data.data.specs
        }).catch(error => {
            console.log(error)
        })
    }
}
</script>

<style scoped>
@import url('@/assets/professions.css');
</style>