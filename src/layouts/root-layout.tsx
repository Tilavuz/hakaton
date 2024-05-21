import Header from "@/components/header";
import SiteBar from "@/components/site-bar";
import { Outlet } from "react-router-dom";

export default function RootLayout() {
  return (
    <div className="flex">
        <div className="max-w-[20vw] w-full border-r">
          <SiteBar />
        </div>
        <div className="flex flex-col w-full">
          <div className="h-[7vh] border-b">
            <Header />
          </div>
          <div className="overflow-y-scroll h-[93vh] p-6">
            <Outlet />
          </div>
        </div>
    </div>
  )
}
