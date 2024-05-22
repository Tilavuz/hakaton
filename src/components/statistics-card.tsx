import { Card, CardContent, CardDescription, CardHeader } from '@/components/ui/card'
import { Users } from 'lucide-react'
import { Badge } from './ui/badge'

export default function StatisticsCard({ title, total }: { title: string, total: number }){
  return (
    <Card className="w-[250px] cursor-pointer select-none">
        <CardHeader>
            <CardDescription className='font-bold text-black dark:text-white'>{title}</CardDescription>
        </CardHeader>
        <CardContent>
            <div className='flex justify-between items-center'>
                <h3 className='font-bold dark:text-white'>{total}</h3>
                <Badge
                  variant="outline"
                  className="flex justify-center items-center size-[43px] rounded-full bg-[#408A7E]"
                >
            <Users size={28} color="white" />
          </Badge>
            </div>
        </CardContent>
    </Card>
  )
}