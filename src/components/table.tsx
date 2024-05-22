import { TableDataNemisProps, TableDataProps } from "@/interface/table-data";
import { Eye } from "lucide-react";
import { Link } from "react-router-dom";

const Table = ({ columns, tableData }: { columns: string[], tableData: TableDataProps[] | TableDataNemisProps[] }) => {

  return (
    <table className="table-items w-full">
      <thead>
        <tr>
          <th className="border border-black dark:border-white text-center w-8">T/R</th>
          {columns.map((data, i) => {
            return (
              <th key={i} className="border border-black dark:border-white p-2 text-center">
                {data}
              </th>
            );
          })}
        </tr>
      </thead>
      <tbody>
        {tableData?.map((user, i) => {
          return (
            <tr
              key={i}
              className={`${i % 2 === 0 ? "bg-[#e6fffb] dark:bg-slate-600" : "bg-white dark:bg-inherit"}`}
            >
              {Object.keys(user).map((title, i) => {
                return (
                  <td key={i} className="border border-black dark:border-white text-left p-2">
                    {title === 'url' ? <Link to={user[title]} className="flex justify-center"> <Eye color="#408a7e" /> </Link> : user[title as keyof typeof user] }
                  </td>
                );
              })}
            </tr>
          );
        })}
      </tbody>
    </table>
  );
};

export default Table;