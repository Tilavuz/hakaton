import { Button } from "@/components/ui/button";
import { Link } from "react-router-dom";

export default function ErrorPage() {
  return (
    <div className="flex flex-col	aligin-center justify-center">
      <p className="text-7xl font-mono mt-[30vh] mb-[50px] text-center ">404. Sahifa topilmadi</p>
      <Button variant={'link'}>
        <Link to={'/'}>Go home Page</Link>
      </Button>
    </div>
  );
}