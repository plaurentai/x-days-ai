flowchart TD
    A(["Start"]) --> B["Get two slices of bread"]
    B --> C["Get peanut butter"]
    C --> D["Get knife"]
    D --> E["Get napkin"]
    E --> F["Lay bread on napkin"]
    F --> G["Spread the peanut butter on slice 1"]
    G --> H["Spread the Jelly on slice 2"]
    H --> I{"Do you want to cut it in half?"}
    I --> |Yes| J["Get a knife"]
    J --> K["Cut it in half"]
    I --> |No| L["Eat your sandwich"]
    K --> L
    L --> M(["End"])
