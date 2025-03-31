/* eslint-disable @typescript-eslint/no-explicit-any */

import { Select, SelectTrigger, SelectValue, SelectContent, SelectItem } from "@/components/ui/select";
import { Input } from "@/components/ui/input";

type FormFieldType = "text" | "number" | "select" | "url";

interface FormFieldMetadata {
    name: string;
    label: string;
    type: FormFieldType;
    placeholder?: string;
    options?: Array<{ value: string; label: string }>;
    isOptional?: boolean;
}

export function createFormFieldMetadata(
    name: string,
    label: string,
    type: FormFieldType = "text",
    placeholder?: string,
    options?: Array<{ value: string; label: string }>,
    isOptional: boolean = false
): FormFieldMetadata {
    return {
        name,
        label: isOptional ? `${label} (Optional)` : label,
        type,
        placeholder: placeholder || `Enter ${label.toLowerCase()}`,
        options,
        isOptional
    };
}

export function renderFormField(
    field: any,
    metadata: FormFieldMetadata,
    onChange?: (value: string) => void
) {
    const { type, placeholder, options } = metadata;

    switch (type) {
        case "select":
            return (
                <Select onValueChange={onChange || field.onChange} defaultValue={field.value}>
                    <SelectTrigger className="w-full">
                        <SelectValue placeholder={placeholder} />
                    </SelectTrigger>
                    <SelectContent>
                        {options?.map((option) => (
                            <SelectItem key={option.value} value={option.value}>
                                {option.label}
                            </SelectItem>
                        ))}
                    </SelectContent>
                </Select>
            );
        case "number":
            return <Input type="number" placeholder={placeholder} {...field} />;
        case "url":
            return <Input type="url" placeholder={placeholder} {...field} />;
        default:
            return <Input placeholder={placeholder} {...field} />;
    }
}
