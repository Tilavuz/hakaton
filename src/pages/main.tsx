import BarsDataset from "@/components/bars-dataset"
import StatisticsCard from "@/components/statistics-card"
import { statistc } from "@/contexts/datas"

export default function Main() {

  return (
    <div>
      <div className="flex gap-4 items-center justify-between mb-12">
        {
          statistc?.map((item, i) => {
            return <StatisticsCard key={i} data={item}/>
          })
        }
      </div>
      <div className="w-full">
        <BarsDataset />
      </div>
    </div>
  )
}
