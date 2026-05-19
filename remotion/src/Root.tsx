import { Composition } from "remotion";
import { PonyPostReel } from "./PonyPostReel";
import { VIDEO } from "./theme";

export const Root: React.FC = () => {
  return (
    <>
      <Composition
        id="PonyPostReel"
        component={PonyPostReel}
        durationInFrames={VIDEO.durationInFrames}
        fps={VIDEO.fps}
        width={VIDEO.width}
        height={VIDEO.height}
      />
    </>
  );
};
