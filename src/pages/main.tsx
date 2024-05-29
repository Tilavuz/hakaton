import BarsDataset from "@/components/bars-dataset"
import StatisticsCard from "@/components/statistics-card"
import TabsComponent from "@/components/tabs-component"
import { statistc } from "@/contexts/datas"

export default function Main() {

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
