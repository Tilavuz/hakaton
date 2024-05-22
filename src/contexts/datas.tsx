import { PieChart, User } from "lucide-react"


export const statistc = [
    {
        title: "Jami xorihiy tillarga o'qitilayotganlar soni",
        total: 3306,
    },
    {
        title: "Inglis tiliga o'qitilayotgan yoshlar soni (C1)",
        total: 1303,
    },
    {
        title: "Inglis tiliga o'qitilayotgan yoshlar soni (B2)",
        total: 206,
    },
    {
        title: "Nemis tiliga o'qitilayotgan yoshlar soni (C1)",
        total: 97,
    },
    {
        title: "Nemis tiliga o'qitilayotgan yoshlar soni (B2)",
        total: 32,
    }
]

export const menuList = [
    {
        title: 'Statistics',
        path: '/',
        icon: <PieChart />
    },
    {
      title: 'Profile',
      path: '/profile',
      icon: <User />
  },
]

export const columnFuture = [
    "Hududlar",
    "Jami xorijiy tillarga o'qitilishi kerak bo'lgan yoshlar soni",
    "Ingliz tiliga o'qitilishi kerak bo'lgan yoshlar soni (B2)",
    "Ingliz tiliga o'qitilishi kerak bo'lgan yoshlar soni (C1)",
    "Nemis tiliga o'qitilishi kerak bo'lgan yoshlar soni (C1)",
    "Nemis tiliga o'qitilishi kerak bo'lgan yoshlar soni (B2)",
    "Ko'rish",
  ];
export const TargetIndicatorsFuture= [
    {
      id: 1,
      region: "Muborak",
      students: 179,
      english: 154,
      nemis: 25,
      url: "/muborak",
    },
    {
      id: 2,
      region: "Qarshi sh",
      students: 485,
      english: 399,
      nemis: 86,
      url: "/qarshi",
    },
    {
      id: 3,
      region: "Qarshi t",
      students: 415,
      english: 357,
      nemis: 61,
      url: "/qarshi",
    },
    {
      id: 4,
      region: "G'uzor t",
      students: 365,
      english: 314,
      nemis: 51,
      url: "/guzor",
    },
    {
      id: 5,
      region: "Dehqonobod",
      students: 386,
      english: 332,
      nemis: 54,
      url: "/dehqanabot",
    },
    {
      id: 6,
      region: "Qamashi t",
      students: 436,
      english: 375,
      nemis: 61,
      url: "/qamashi",
    },
    {
      id: 7,
      region: "Kasbi t",
      students: 300,
      english: 258,
      nemis: 42,
      url: "/kasbi",
    },
    {
      id: 8,
      region: "Kitob t",
      students: 422,
      english: 363,
      nemis: 59,
      url: "/kitob",
    },
    {
      id: 9,
      region: "Koson t",
      students: 558,
      english: 480,
      nemis: 78,
      url: "/koson",
    },
    {
      id: 10,
      region: "Mirishkor t",
      students: 286,
      english: 246,
      nemis: 40,
      url: "/mirishkor",
    },
    {
      id: 11,
      region: "Nishon t",
      students: 286,
      english: 246,
      nemis: 40,
      url: "/nishon",
    },
    {
      id: 12,
      region: "Shaxrisabz sh",
      students: 286,
      english: 246,
      nemis: 40,
      url: "/shaxrisabz",
    },
    {
      id: 13,
      region: "Shaxrisabz t",
      students: 408,
      english: 351,
      nemis: 57,
      url: "/shaxrisabz",
    },
    {
      id: 14,
      region: "Chiroqchi t",
      students: 422,
      english: 363,
      nemis: 59,
      url: "/chiroqchi",
    },
    {
      id: 15,
      region: "Yakkabog' t",
      students: 450,
      english: 387,
      nemis: 63,
      url: "/yakkabog",
    },
    {
      id: 16,
      region: "Ko'kdala t",
      students: 266,
      english: 229,
      nemis: 37,
      url: "/kokdala",
    },
  ];

  export const TargetIndicatorsNow = [
    {
      id: 1,
      region: "Muborak",
      studentNow: 363,
      studentEnglish: 163,
      foizEnglish: "40%" ,
      studentNemis: 80,
      foizNemis: 60,
      studentEnglishPast: 32,
      studentNemisPast:34,
      url: "/muborak",
    },
    {
      id: 2,
      region: "Qarshi sh",
      students: 485,
      english: 80,
      nemis: 32,
      url: "/qarshi",
    },
    {
      id: 3,
      region: "Qarshi t",
      students: 363,
      english: 80,
      nemis: 32,
      url: "/qarshi",
    },
    {
      id: 4,
      region: "G'uzor t",
      students: 363,
      english: 80,
      nemis: 32,
      url: "/guzor",
    },
    {
      id: 5,
      region: "Dehqanabot",
      students: 363,
      english: 80,
      nemis: 32,
      url: "/dehqanabot",
    },
    {
      id: 6,
      region: "Qamashi t",
      students: 363,
      english: 80,
      nemis: 32,
      url: "/qamashi",
    },
    {
      id: 7,
      region: "Kasbi t",
      students: 363,
      english: 80,
      nemis: 32,
      url: "/kasbi",
    },
    {
      id: 8,
      region: "Kitob t",
      students: 363,
      english: 80,
      nemis: 32,
      url: "/kitob",
    },
    {
      id: 9,
      region: "Koson t",
      students: 363,
      english: 80,
      nemis: 32,
      url: "/koson",
    },
    {
      id: 10,
      region: "Mirishkor t",
      students: 363,
      english: 80,
      nemis: 32,
      url: "/mirishkor",
    },
    {
      id: 11,
      region: "Nishon t",
      students: 363,
      english: 80,
      nemis: 32,
      url: "/nishon",
    },
    {
      id: 12,
      region: "Shaxrisabz sh",
      students: 363,
      english: 80,
      nemis: 32,
      url: "/shaxrisabz",
    },
    {
      id: 13,
      region: "Shaxrisabz t",
      students: 363,
      english: 80,
      nemis: 32,
      url: "/shaxrisabz",
    },
    {
      id: 14,
      region: "Chiroqchi t",
      students: 363,
      english: 80,
      nemis: 32,
      url: "/chiroqchi",
    },
    {
      id: 15,
      region: "Yakkabog' t",
      students: 363,
      english: 80,
      nemis: 32,
      url: "/yakkabog",
    },
    {
      id: 16,
      region: "Ko'kdala t",
      students: 363,
      english: 80,
      nemis: 32,
      url: "/kokdala",
    },
  ];

export const columns = [
    "Hududlar",
    "Jami xorijiy tillarga o'qitilishi kerak bo'lgan yoshlar soni",
    "Ingliz tiliga o'qitilishi kerak bo'lgan yoshlar soni (B2)",
    "Ingliz tiliga o'qitilishi kerak bo'lgan yoshlar soni (C1)",
    "Nemis tiliga o'qitilishi kerak bo'lgan yoshlar soni (C1)",
    "Nemis tiliga o'qitilishi kerak bo'lgan yoshlar soni (B2)",
    "Ko'rish",
  ];
  export const columnNow = [
    "Hududlar",
    "Jami xorijiy tillarga o'qitilayotgan yoshlar soni",
    "Jami ingliz tiliga o'qitilayotgan yoshlar soni",
    "Foiz",
    "Jami nemis tiliga o'qitilayotgan yoshlar soni",
    "Foiz",
    "Jami ingliz tilida sertifikatga ega yoshlar soni",
    "Jami nemis tilida sertifikatga ega yoshlar soni",
    "Ko'rish",
  ];

  export const columnEnglish = [
    "Hududlar",
    "Jami ingliz tiliga qiziquvchi yoshlar soni",
    "Jami ingliz tiliga o'qitilayotgan yoshlar soni	",
    "Foiz",
    "Jami ingliz tilida (B2) sertifikatga o'qitilyotgan yoshlar soni",
    "Jami ingliz tilida (C1) sertifikatga o'qitilyotgan yoshlar soni",
    "Jami ingliz tilidan sertifikat olgan yoshlar soni",
    "Foiz",
    "Jami ingliz tilida (B2) sertifikatga ega yoshlar soni",
    "Jami ingliz tilida (C1) sertifikatga ega yoshlar soni",
    "Ko'rish",
  ];
  export const columnNemis = [
    "Hududlar",
    "Jami nemis tiliga qiziquvchi yoshlar soni",
    "Jami nemis tiliga o'qitilayotgan yoshlar soni	",
    "Foiz",
    "Jami nemis tilida (B2) sertifikatga o'qitilyotgan yoshlar soni",
    "Jami nemis tilida (C1) sertifikatga o'qitilyotgan yoshlar soni",
    "Jami nemis tilidan sertifikat olgan yoshlar soni",
    "Foiz",
    "Jami nemis tilida (B2) sertifikatga ega yoshlar soni",
    "Jami nemis tilida (C1) sertifikatga ega yoshlar soni",
    "Ko'rish",
  ];


export const organization = [
  {
    "id": 1,
    "region": "1-maktab",
    "students": 33,
    "english": 13,
    "englishFoiz": "40%",
    "nemis": 20,
    "nemisFoiz": "60%",
    "url": "/qashqadaryo/muborak/1-maktab"
  },
  {
    "id": 2,
    "region": "2-maktab",
    "students": 45,
    "english": 20,
    "englishFoiz": "44%",
    "nemis": 25,
    "nemisFoiz": "56%",
    "url": "/qashqadaryo/muborak/2-maktab"
  },
  {
    "id": 3,
    "region": "3-maktab",
    "students": 55,
    "english": 30,
    "englishFoiz": "55%",
    "nemis": 25,
    "nemisFoiz": "45%",
    "url": "/qashqadaryo/muborak/3-maktab"
  },
  {
    "id": 4,
    "region": "4-maktab",
    "students": 40,
    "english": 18,
    "englishFoiz": "45%",
    "nemis": 22,
    "nemisFoiz": "55%",
    "url": "/qashqadaryo/muborak/4-maktab"
  },
  {
    "id": 5,
    "region": "5-maktab",
    "students": 60,
    "english": 24,
    "englishFoiz": "40%",
    "nemis": 36,
    "nemisFoiz": "60%",
    "url": "/qashqadaryo/muborak/5-maktab"
  },
  {
    "id": 6,
    "region": "6-maktab",
    "students": 70,
    "english": 25,
    "englishFoiz": "36%",
    "nemis": 45,
    "nemisFoiz": "64%",
    "url": "/qashqadaryo/muborak/6-maktab"
  },
  {
    "id": 7,
    "region": "7-maktab",
    "students": 80,
    "english": 30,
    "englishFoiz": "38%",
    "nemis": 50,
    "nemisFoiz": "62%",
    "url": "/qashqadaryo/muborak/7-maktab"
  },
  {
    "id": 8,
    "region": "8-maktab",
    "students": 65,
    "english": 28,
    "englishFoiz": "43%",
    "nemis": 37,
    "nemisFoiz": "57%",
    "url": "/qashqadaryo/muborak/8-maktab"
  },
  {
    "id": 9,
    "region": "9-maktab",
    "students": 55,
    "english": 20,
    "englishFoiz": "36%",
    "nemis": 35,
    "nemisFoiz": "64%",
    "url": "/qashqadaryo/muborak/9-maktab"
  },
  {
    "id": 10,
    "region": "10-maktab",
    "students": 75,
    "english": 30,
    "englishFoiz": "40%",
    "nemis": 45,
    "nemisFoiz": "60%",
    "url": "/qashqadaryo/muborak/10-maktab"
  },
  {
    "id": 11,
    "region": "11-maktab",
    "students": 90,
    "english": 40,
    "englishFoiz": "44%",
    "nemis": 50,
    "nemisFoiz": "56%",
    "url": "/qashqadaryo/muborak/11-maktab"
  },
  {
    "id": 12,
    "region": "12-maktab",
    "students": 65,
    "english": 30,
    "englishFoiz": "46%",
    "nemis": 35,
    "nemisFoiz": "54%",
    "url": "/qashqadaryo/muborak/12-maktab"
  },
  {
    "id": 13,
    "region": "13-maktab",
    "students": 55,
    "english": 22,
    "englishFoiz": "40%",
    "nemis": 33,
    "nemisFoiz": "60%",
    "url": "/qashqadaryo/muborak/13-maktab"
  },
  {
    "id": 14,
    "region": "14-maktab",
    "students": 80,
    "english": 35,
    "englishFoiz": "43%",
    "nemis": 45,
    "nemisFoiz": "57%",
    "url": "/qashqadaryo/muborak/14-maktab"
  },
  {
    "id": 15,
    "region": "15-maktab",
    "students": 70,
    "english": 28,
    "englishFoiz": "40%",
    "nemis": 42,
    "nemisFoiz": "60%",
    "url": "/qashqadaryo/muborak/15-maktab"
  }
]

