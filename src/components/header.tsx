import { Menu } from "lucide-react";
import { ModeToggle } from "./mode-toggle";
import { useContext } from "react";
import { MenuContext } from "@/contexts/toggle-menu";
import { DropdownMenu, DropdownMenuTrigger } from "@radix-ui/react-dropdown-menu";
import { DropdownMenuContent, DropdownMenuGroup, DropdownMenuItem, DropdownMenuSeparator } from "./ui/dropdown-menu";
import { Link } from "react-router-dom";
import colorRed from '../constants/style'

export default function Header() {


  const { handleMenu } = useContext(MenuContext)
  
  return (
    <header className="h-full flex justify-between items-center px-4">
        <div className="">
            <button onClick={() => handleMenu()}>
                <Menu size={24}/>
            </button>
        </div>
        <div className="flex items-center gap-4">
          <ModeToggle />
          <DropdownMenu>
            <DropdownMenuTrigger>
              <div className="flex items-center gap-2 cursor-pointer">
                <div>
                  <img width={`60px`} height={`60px`} className="rounded-full" src="https://firebasestorage.googleapis.com/v0/b/total-array-422417-i0.appspot.com/o/logo.png?alt=media&token=ae58c251-6c64-4aca-873b-1b2942b6e9d9" alt="image" />
                </div>
                <div>
                  <p className="font-bold">Tilovov Shavqiddin</p>
                  <p className="font-thin text-left">329472190471</p>
                </div>
              </div>
            </DropdownMenuTrigger>
            <DropdownMenuContent>
                        <DropdownMenuGroup>
                            <DropdownMenuItem className='p-0'>
                                <Link className="w-full py-[6px] px-[8px] h-full" to={'/profile'}>Profile</Link>
                            </DropdownMenuItem>
                            <DropdownMenuItem>Shaxsiy ma'lumotlarim</DropdownMenuItem>
                        </DropdownMenuGroup>
                        <DropdownMenuSeparator />
                        <DropdownMenuItem className={`text-${colorRed} font-bold`}>Chiqish</DropdownMenuItem>
                    </DropdownMenuContent>
          </DropdownMenu>
        </div>
    </header>
  )
}
