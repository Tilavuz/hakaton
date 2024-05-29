import BarsDataset from "@/components/bars-dataset"
import StatisticsCard from "@/components/statistics-card"
import TabsComponent from "@/components/tabs-component"
import { statistc } from "@/contexts/datas"
import { useEffect } from "react"
import axios from 'axios'
const token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2ODA5NDA2LCJpYXQiOjE3MTYzNzc0MDYsImp0aSI6IjIwNDI3MWMzOTYwZTQ3NzE5N2JjODRlNGMyMDAxOGE0IiwidXNlcl9pZCI6MX0.aPSRY5gc3oWHrIm-qFpAVchIvy8DoIWdu0nb09_Kq5c"

export default function Main() {

  useEffect(() => {
    const getStatistics = async () => {
      try {
        const res = await axios.get('http://0.0.0.0:8000/statistika/viloyat', {
          headers: {
            "Authorization": `Bearer ${token}`
          }
        });
        console.log(res);
      } catch (error) {
        console.error('Error fetching statistics:', error);
      }
    };
    
    getStatistics();
  }, []);

  return (
    <div>
      <div className="flex gap-4 items-center justify-between mb-12">
        {
          statistc?.map((item, i) => {
            return <StatisticsCard key={i} title={item.title} total={item.total}/>
          })
        }
      </div>
      <div className="w-full">
        <h2 className="uppercase font-bold text-center text-2xl py-8"><i>qashqadaryo</i> viloyatining tumanlar aro statistikasi</h2>
        <BarsDataset />
      </div>
      <div>
        <h2 className="uppercase font-bold text-center text-2xl py-8">Loyiha doirasida shakillangan ko'rsatkichlar jadvali</h2>
        <TabsComponent />
      </div>
    </div>
  )
}
