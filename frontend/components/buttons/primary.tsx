import { Button } from "@/components/ui/button";
import { LucideIcon } from "lucide-react";
import { cn } from "@/lib/utils";

interface PrimaryButtonProps {
    icon?: LucideIcon;
    onClick?: () => void;
    children: React.ReactNode;
    className?: string;
    size?: "default" | "sm" | "lg" | "icon";
    variant?: "default" | "outline" | "ghost" | "link";
    asChild?: boolean;
    disabled?: boolean;
}

export default function PrimaryButton({
    icon: Icon,
    onClick,
    children,
    className,
    size = "lg",
    variant = "default",
    asChild = false,
    disabled = false
}: PrimaryButtonProps) {
    return (
        <Button 
            size={size} 
            className={cn("cursor-pointer", className)}
            onClick={onClick}
            variant={variant}
            asChild={asChild}
            disabled={disabled}
        >
            {Icon && <Icon />}
            {children}
        </Button>
    );
}
