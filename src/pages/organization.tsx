import Table from "@/components/table";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { columnNeighborhood, studentsBobur } from "@/contexts/datas";

export default function Organization() {
  return (
    <div className="w-full">
        <div className="flex items-center justify-between mb-12">
            <p className="font-bold text-2xl capitalize">Bobur mahallasi</p>
            <div className="flex gap-2">
                <Input placeholder="Search" className="w-[400px]" />
                <Button>Qidirish</Button>
            </div>
        </div>
        <Table columns={columnNeighborhood} tableData={studentsBobur} />
    </div>
  )
}
