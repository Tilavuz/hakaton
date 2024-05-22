import { TargetIndicators } from '@/contexts/datas'
import { columns } from '@/contexts/datas'
import Table from './table'
import { TabsContent, Tabs, TabsList, TabsTrigger } from './ui/tabs'

export default function TabsComponent() {
  return (
    <Tabs defaultValue="Maqsadli ko'rsatkichlar">
        <TabsList className="flex">
            <TabsTrigger value="Maqsadli ko'rsatkichlar">Maqsadli ko'rsatkichlar</TabsTrigger>
            <TabsTrigger value="Jami o'qiyotganlar ko'rsatkichlar">Jami o'qiyotganlar ko'rsatkichlar</TabsTrigger>
            <TabsTrigger value="Ingliz tili o'qiyotganlar ko'rsatkichlar">Ingliz tili o'qiyotganlar ko'rsatkichlar</TabsTrigger>
            <TabsTrigger value="Nemis tiliga o'qiyotganlar ko'rsatkichlar">Nemis tiliga o'qiyotganlar ko'rsatkichlar</TabsTrigger>
        </TabsList>
        <TabsContent value="Maqsadli ko'rsatkichlar">
          <Table columns={columns} tableData={TargetIndicators}/>
        </TabsContent>
        <TabsContent value="Jami o'qiyotganlar ko'rsatkichlar">
          <Table columns={columns} tableData={TargetIndicators}/>
        </TabsContent>
        <TabsContent value="Ingliz tili o'qiyotganlar ko'rsatkichlar">
          <Table columns={columns} tableData={TargetIndicators}/>
        </TabsContent>
        <TabsContent value="Nemis tiliga o'qiyotganlar ko'rsatkichlar">
          <Table columns={columns} tableData={TargetIndicators}/>
        </TabsContent>
    </Tabs>
  )
}