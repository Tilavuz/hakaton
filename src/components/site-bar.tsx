import { menuList } from "@/contexts/datas";
import { NavLink } from "react-router-dom";

export default function SiteBar() {
  return (
    <aside className="w-full h-screen">
        <div className="h-[7vh] flex justify-center items-center border-b">
            <h1 className="font-bold text-2xl">Dashboard</h1>
        </div>
        <ul className="pt-8 flex flex-col">
          {
            menuList?.map((menu, i) => {
              return <li className="h-12" key={i}>
                <NavLink className="menu dark:text-white px-4 h-full flex items-center gap-2 font-bold" to={menu.path}>
                  {
                    menu.icon
                  }
                  {menu.title}
                </NavLink>
              </li>
            })
          }
        </ul>
    </aside>
  )
}
