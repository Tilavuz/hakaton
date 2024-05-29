import StatisticsCard from "@/components/statistics-card";
import {
  statistc,
} from "@/contexts/datas";
import {
  Pagination,
  PaginationContent,
  PaginationEllipsis,
  PaginationItem,
  PaginationLink,
  PaginationNext,
  PaginationPrevious,
} from "@/components/ui/pagination";
import { useParams } from "react-router-dom";
import TabsOrganization from "@/components/tabs-organization";

export default function District() {

  const { district } = useParams()
  return (
    <div className="">
      <h1 className="uppercase font-bold text-center text-2xl pb-8">{district} tumani</h1>
      <div className="flex items-center gap-5 flex-wrap justify-between">
        {statistc.map((data, i) => {
          if (data.total) {
            return <StatisticsCard key={i} title={data.title} total={data.total} />;
          }
        })}
      </div>
      <div className="mb-8">
        <h3 className="text-center font-bold p-4 text-xl">
          LOYIHA DOIRASIDA SHAKILLANTIRILGAN KO'RSATKICHLAR JADVALI
        </h3>
        <TabsOrganization/>
      </div>
      <Pagination>
        <PaginationContent>
          <PaginationItem>
            <PaginationPrevious href="#" />
          </PaginationItem>
          <PaginationItem>
            <PaginationLink href="#">1</PaginationLink>
          </PaginationItem>
          <PaginationItem>
            <PaginationLink href="#" isActive>
              2
            </PaginationLink>
          </PaginationItem>
          <PaginationItem>
            <PaginationLink href="#">3</PaginationLink>
          </PaginationItem>
          <PaginationItem>
            <PaginationEllipsis />
          </PaginationItem>
          <PaginationItem>
            <PaginationNext href="#" />
          </PaginationItem>
        </PaginationContent>
      </Pagination>
    </div>
  );
}
