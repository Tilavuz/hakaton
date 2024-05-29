import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

export default function Organization() {
  return (
    <div className="w-full">
        <div className="flex items-center justify-between">
            <p className="font-bold text-2xl capitalize">Bobur mahallasi</p>
            <div className="flex gap-2">
                <Input placeholder="Search" className="w-[400px]" />
                <Button>Qidirish</Button>
            </div>
        </div>
    </div>
  )
}
