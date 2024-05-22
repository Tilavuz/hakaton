import { TableDataProps } from "@/interface/table-data";
import { Eye } from "lucide-react";
import { Link } from "react-router-dom";

const Table = ({ columns, tableData }: { columns: string[], tableData: TableDataProps[] }) => {

  return (
    <table className="table-items">
      <thead>
        <tr>
          <th className="border border-black text-center w-8">T/R</th>
          {columns.map((data, i) => {
            return (
              <th key={i} className="border border-black p-2 text-center">
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
              className={`${i % 2 === 0 ? "bg-[#e6fffb]" : "bg-white"}`}
            >
              {Object.keys(user).map((title, i) => {
                return (
                  <td key={i} className="border border-black text-left p-2">
                    {title === 'url' ? <Link to={user[title]} className="flex justify-center"> <Eye color="#408a7e" /> </Link> : user[title] }
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