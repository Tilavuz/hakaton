import { columnEnglish, columnNemis, columnPurposeful, columnsDone, rowsEnglish, organizationNemis, targetIndicatorsFuture } from "@/contexts/datas";
import Table from "./table";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "./ui/tabs";

export default function TabsOrganization() {
  return (
    <Tabs defaultValue="Maqsadli ko'rsatkichlar">
        <TabsList className="flex">
            <TabsTrigger value="Maqsadli ko'rsatkichlar">Maqsadli ko'rsatkichlar</TabsTrigger>
            <TabsTrigger value="Jami o'qiyotganlar ko'rsatkichlar">Jami o'qiyotganlar ko'rsatkichlar</TabsTrigger>
            <TabsTrigger value="Ingliz tili o'qiyotganlar ko'rsatkichlar">Ingliz tili o'qiyotganlar ko'rsatkichlar</TabsTrigger>
            <TabsTrigger value="Nemis tiliga o'qiyotganlar ko'rsatkichlar">Nemis tiliga o'qiyotganlar ko'rsatkichlar</TabsTrigger>
        </TabsList>
        <TabsContent value="Maqsadli ko'rsatkichlar">
          <Table columns={columnPurposeful} tableData={targetIndicatorsFuture}/>
        </TabsContent>
        <TabsContent value="Jami o'qiyotganlar ko'rsatkichlar">
          <Table columns={columnsDone} tableData={targetIndicatorsFuture}/>
        </TabsContent>
        <TabsContent value="Ingliz tili o'qiyotganlar ko'rsatkichlar">
          <Table columns={columnEnglish} tableData={rowsEnglish}/>
        </TabsContent>
        <TabsContent value="Nemis tiliga o'qiyotganlar ko'rsatkichlar">
          <Table columns={columnNemis} tableData={organizationNemis}/>
        </TabsContent>
    </Tabs>
  )
}
