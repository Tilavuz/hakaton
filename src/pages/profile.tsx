import { Card, CardContent, CardDescription, CardHeader } from "@/components/ui/card";
import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";

export default function Profile() {
  return (
    <Card className='max-w-[900px]'>
        <CardHeader className='border-b py-[10px]'>
            <CardDescription className='font-bold text-base'>Profilim</CardDescription>
        </CardHeader>
        <CardContent className='p-6'>
            <form className="">
                <div className="flex items-center gap-16 mb-6">
                    <div>
                        <img className="w-[120px] h-[140px]" src="https://redchili21.my/wp-content/uploads/2020/09/3.jpg" alt="profile image" />
                    </div>
                    <div className="flex gap-8">
                        <Label className='flex flex-col gap-2'>
                            <span className="font-bold">Seriyasi va raqami</span>
                            <Input type="text" className="uppercase" disabled value="AB 123456"/>
                        </Label>
                        <Label className='flex flex-col gap-2'>
                            <span className="font-bold">Tug'ilgan sanasi</span>
                            <Input type="date" className="uppercase" disabled value="1899-01-02"/>
                        </Label>
                    </div>
                </div>
                <div className="border-b-2 pb-6 mb-6">
                    <div className="flex items-center gap-4 mb-6">
                        <Label className='flex-1 flex flex-col gap-2'>
                            <span className="font-bold">Familyasi</span>
                            <Input type="text" className="uppercase" disabled value="Tilovov"/>
                        </Label>
                        <Label className='flex-1 flex flex-col gap-2'>
                            <span className="font-bold">Ismi</span>
                            <Input type="text" className="uppercase" disabled value="Shavqiddin"/>
                        </Label>
                    </div>
                    <div className="flex items-center gap-4">
                        <Label className='flex-1 flex flex-col gap-2'>
                            <span className="font-bold">Otasining ismi</span>
                            <Input type="text" className="uppercase" disabled value="Sayfiddin"/>
                        </Label>
                        <Label className='flex-1 flex flex-col gap-2'>
                            <span className="font-bold">Tug'ilgan joyi</span>
                            <Input type="text" className="uppercase" disabled value="Qashqadaryo viloyati Koson tumani"/>
                        </Label>
                    </div>
                </div>
                <div className="pb-6">
                    <div className="flex items-center gap-4 mb-6">
                        <Label className='flex-1 flex flex-col gap-2'>
                            <span className="font-bold">Viloyat</span>
                            <Input type="text" className="uppercase" value="Qashqadaryo"/>
                        </Label>
                        <Label className='flex-1 flex flex-col gap-2'>
                            <span className="font-bold">Tuman</span>
                            <Input type="text" className="uppercase" value="Muborak"/>
                        </Label>
                    </div>
                    <div className="flex items-center gap-4">
                        <Label className='flex-1 flex flex-col gap-2'>
                            <span className="font-bold">MFY</span>
                            <Input type="text" className="uppercase" value="Tong"/>
                        </Label>
                        <Label className='flex-1 flex flex-col gap-2'>
                            <span className="font-bold">PINFL</span>
                            <Input type="text" className="uppercase" disabled value="4560468464642"/>
                        </Label>
                    </div>
                </div>
                <div className="flex gap-4 mb-6 border-b-2 pb-6">
                    <Label className='flex-1 flex flex-col gap-2'>
                        <span className="font-bold">Millat</span>
                        <Input type="text" className="uppercase" disabled value="uzbek"/>
                    </Label>
                    <Label className='flex-1 flex flex-col gap-2'>
                        <span className="font-bold">Jinsi</span>
                        <Input type="text" className="uppercase" disabled value="erkak"/>
                    </Label>
                    <Label className='flex-1 flex flex-col gap-2'>
                        <span className="font-bold">Telefon raqam</span>
                        <Input type="text" className="uppercase" value="+998 90 882 7251"/>
                    </Label>
                </div>
                <div className="flex gap-4 mb-6">
                    <Label className='flex-1 flex flex-col gap-2'>
                        <span className="font-bold">Lavozimi</span>
                        <Input type="text" className="uppercase" disabled value="MFY inspektori"/>
                    </Label>
                    <Label className='flex-1 flex flex-col gap-2'>
                        <span className="font-bold">Unvoni</span>
                        <Input type="text" className="uppercase" disabled value="Mayor"/>
                    </Label>
                </div>
                <div className="flex items-center justify-end">
                    <Button className='' variant={'outline'}>Saqlash</Button>
                </div>
            </form>
        </CardContent>
    </Card>
  )
}