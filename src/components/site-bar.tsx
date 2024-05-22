import { menuList } from "@/contexts/datas";
import { MenuContext } from "@/contexts/toggle-menu";
import { useContext } from "react";
import { NavLink } from "react-router-dom";

export default function SiteBar() {

  const {isOpen} = useContext(MenuContext)

  return (
    <aside className={`h-screen ${isOpen ? 'w-[20vw]' : ''}`}>
        <div className="h-[7vh] flex justify-center items-center border-b">
            <h1 className={`font-bold text-2xl ${isOpen ? '' : 'hidden'}`}>Dashboard</h1>
        </div>
        <ul className="pt-8 flex flex-col">
          {
            menuList?.map((menu, i) => {
              return <li className="h-12" key={i}>
                <NavLink className={`menu dark:text-white px-4 h-full flex items-center gap-2 font-bold hover:underline ${isOpen ? '' : 'justify-center'}`} to={menu.path}>
                  {
                    menu.icon
                  }
                  {isOpen ? menu.title : ''}
                </NavLink>
              </li>
            })
          }
        </ul>
    </aside>
  )
}
