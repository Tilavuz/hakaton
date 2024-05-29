import { ReactNode, createContext, useState } from "react"

interface MenuContextType {
    isOpen: boolean;
    handleMenu: () => void;
}

const defaultValue: MenuContextType = {
    isOpen: true,
    handleMenu: () => {}, 
  };

export const MenuContext = createContext<MenuContextType>(defaultValue)

interface ToggleMenuProps {
    children: ReactNode
}

export default function ToggleMenu({ children }: ToggleMenuProps) {
    const [isOpen, setIsOpen] = useState<boolean>(true)
    const handleMenu = () => {
        setIsOpen(!isOpen)
    }
  return (
    <MenuContext.Provider value={{ handleMenu, isOpen }}>
        {children}
    </MenuContext.Provider>
  )
}
