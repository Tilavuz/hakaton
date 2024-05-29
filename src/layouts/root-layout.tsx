import Header from "@/components/header";
import SiteBar from "@/components/site-bar";
import ToggleMenu from "@/contexts/toggle-menu";
import { Outlet } from "react-router-dom";

export default function RootLayout() {
  return (
    <ToggleMenu>
      <div className="flex">
          <div className="border-r w-max dark:border-r-white">
            <SiteBar />
          </div>
          <div className="flex flex-col w-full">
            <div className="h-[7vh] border-b dark:border-b-white">
              <Header />
            </div>
            <div className="overflow-y-scroll h-[93vh] p-6 pb-24">
              <Outlet />
            </div>
          </div>
      </div>
    </ToggleMenu>
  )
}
