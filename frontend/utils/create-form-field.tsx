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

interface CreateFormFieldMetadataParams {
    name: string;
    label: string;
    type?: FormFieldType;
    placeholder?: string;
    options?: Array<{ value: string; label: string }>;
    isOptional?: boolean;
}

/**
 * Creates metadata for form fields with standardized configuration
 * 
 * @param params - Object containing field configuration
 * @param params.name - The field name/key used in the form data
 * @param params.label - Display label for the form field
 * @param params.type - Type of input field ("text" | "number" | "select" | "url")
 * @param params.placeholder - Custom placeholder text (optional)
 * @param params.options - Array of options for select fields (optional)
 * @param params.isOptional - Whether the field is optional (defaults to false)
 * 
 * @returns FormFieldMetadata object containing field configuration
 * 
 * @example
 * // Basic text field
 * createFormFieldMetadata({ name: "fullName", label: "Full Name" })
 * 
 * @example
 * // Select field with options
 * createFormFieldMetadata({
 *   name: "language",
 *   label: "Language",
 *   type: "select",
 *   placeholder: "Select language",
 *   options: languages
 * })
 * 
 * @example
 * // Optional URL field
 * createFormFieldMetadata({
 *   name: "portfolioLink",
 *   label: "Portfolio Link",
 *   type: "url",
 *   placeholder: "Enter portfolio URL",
 *   isOptional: true
 * })
 */

export function createFormFieldMetadata(
    params: CreateFormFieldMetadataParams
): FormFieldMetadata {
    const { name, label, type = "text", placeholder, options, isOptional = false } = params;
    
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
