<?xml version="1.0" encoding="UTF-8" ?>
<Package name="Mark 1" format_version="5">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="ExampleDialog" src="behavior_1/ExampleDialog/ExampleDialog.dlg" />
        <Dialog name="helloworld" src="helloworld/helloworld.dlg" />
    </Dialogs>
    <Resources>
        <File name="naatu naatu" src="naatu naatu.mp3" />
        <File name="name" src="name.wav" />
        <File name="heaven1" src="behavior_1/behavior_1/heaven1.ogg" />
    </Resources>
    <Topics>
        <Topic name="ExampleDialog_enu" src="behavior_1/ExampleDialog/ExampleDialog_enu.top" topicName="ExampleDialog" language="en_US" nuance="enu" />
        <Topic name="helloworld_enu" src="helloworld/helloworld_enu.top" topicName="helloworld" language="en_US" nuance="enu" />
    </Topics>
    <IgnoredPaths />
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
    </Translations>
</Package>
