<a id="mopipe.core.segments.inputs"></a>

# mopipe.core.segments.inputs

<a id="mopipe.core.segments.inputs.InputTypeBaseMixin"></a>

## InputTypeBaseMixin Objects

```python
class InputTypeBaseMixin(IOTypeBaseMixin)
```

Mixin class for all segments input types.

<a id="mopipe.core.segments.inputs.InputTypeBaseMixin.input_type"></a>

#### input\_type

```python
@property
def input_type() -> IOType
```

The type of the input.

<a id="mopipe.core.segments.inputs.InputTypeBaseMixin.validate_input"></a>

#### validate\_input

```python
@abstractmethod
def validate_input(**kwargs) -> bool
```

Validate the input.

<a id="mopipe.core.segments.inputs.UnivariateSeriesInput"></a>

## UnivariateSeriesInput Objects

```python
class UnivariateSeriesInput(InputTypeBaseMixin)
```

Mixin class for univariate series input segments.

<a id="mopipe.core.segments.inputs.UnivariateSeriesInput.validate_input"></a>

#### validate\_input

```python
def validate_input(**kwargs) -> bool
```

Validate the input.

<a id="mopipe.core.segments.inputs.MultivariateSeriesInput"></a>

## MultivariateSeriesInput Objects

```python
class MultivariateSeriesInput(InputTypeBaseMixin)
```

Mixin class for multivariate series input segments.

<a id="mopipe.core.segments.inputs.MultivariateSeriesInput.validate_input"></a>

#### validate\_input

```python
def validate_input(**kwargs) -> bool
```

Validate the input.

<a id="mopipe.core.segments.inputs.SingleValueInput"></a>

## SingleValueInput Objects

```python
class SingleValueInput(InputTypeBaseMixin)
```

Mixin class for single value input segments.

<a id="mopipe.core.segments.inputs.SingleValueInput.validate_input"></a>

#### validate\_input

```python
def validate_input(**kwargs) -> bool
```

Validate the input.

<a id="mopipe.core.segments.inputs.MultiValueInput"></a>

## MultiValueInput Objects

```python
class MultiValueInput(InputTypeBaseMixin)
```

Mixin class for multiple values input segments.

<a id="mopipe.core.segments.inputs.MultiValueInput.validate_input"></a>

#### validate\_input

```python
def validate_input(**kwargs) -> bool
```

Validate the input.

<a id="mopipe.core.segments.inputs.SingleNumericValueInput"></a>

## SingleNumericValueInput Objects

```python
class SingleNumericValueInput(InputTypeBaseMixin)
```

Mixin class for single numeric value input segments.

<a id="mopipe.core.segments.inputs.SingleNumericValueInput.validate_input"></a>

#### validate\_input

```python
def validate_input(**kwargs) -> bool
```

Validate the input.

<a id="mopipe.core.segments.inputs.AnySeriesInput"></a>

## AnySeriesInput Objects

```python
class AnySeriesInput(InputTypeBaseMixin)
```

Mixin class for any series input segments.

<a id="mopipe.core.segments.inputs.AnySeriesInput.validate_input"></a>

#### validate\_input

```python
def validate_input(**kwargs) -> bool
```

Validate the input.

<a id="mopipe.core.segments.inputs.AnyNumericInput"></a>

## AnyNumericInput Objects

```python
class AnyNumericInput(InputTypeBaseMixin)
```

Mixin class for any numeric input segments.

<a id="mopipe.core.segments.inputs.AnyNumericInput.validate_input"></a>

#### validate\_input

```python
def validate_input(**kwargs) -> bool
```

Validate the input.

<a id="mopipe.core.segments.inputs.AnyInput"></a>

## AnyInput Objects

```python
class AnyInput(InputTypeBaseMixin)
```

Mixin class for any input segments.

<a id="mopipe.core.segments.inputs.AnyInput.validate_input"></a>

#### validate\_input

```python
def validate_input(**kwargs) -> bool
```

Validate the input.

<a id="mopipe.core.segments.inputs.OtherInput"></a>

## OtherInput Objects

```python
class OtherInput(InputTypeBaseMixin)
```

Mixin class for other input segments.

<a id="mopipe.core.segments.inputs.OtherInput.validate_input"></a>

#### validate\_input

```python
def validate_input(**kwargs) -> bool
```

Validate the input.

<a id="mopipe.core.segments.io"></a>

# mopipe.core.segments.io

<a id="mopipe.core.segments.io.IOType"></a>

## IOType Objects

```python
class IOType(Enum)
```

Type of segment inputs/outputs.

This is used to determine whether a segment can be run on a given
input, or if the output of a segment can be used as input to another.

<a id="mopipe.core.segments.io.IOTypeBaseMixin"></a>

## IOTypeBaseMixin Objects

```python
class IOTypeBaseMixin()
```

Mixin class for all segments input/output types.

<a id="mopipe.core.segments.outputs"></a>

# mopipe.core.segments.outputs

<a id="mopipe.core.segments.outputs.OutputTypeBaseMixin"></a>

## OutputTypeBaseMixin Objects

```python
class OutputTypeBaseMixin(IOTypeBaseMixin)
```

Mixin class for all segments output types.

<a id="mopipe.core.segments.outputs.OutputTypeBaseMixin.output_type"></a>

#### output\_type

```python
@property
def output_type() -> IOType
```

The type of the output.

<a id="mopipe.core.segments.outputs.OutputTypeBaseMixin.validate_output"></a>

#### validate\_output

```python
@abstractmethod
def validate_output(output: t.Any) -> bool
```

Validate the output.

<a id="mopipe.core.segments.outputs.UnivariateSeriesOutput"></a>

## UnivariateSeriesOutput Objects

```python
class UnivariateSeriesOutput(OutputTypeBaseMixin)
```

Mixin class for univariate series output segments.

<a id="mopipe.core.segments.outputs.UnivariateSeriesOutput.validate_output"></a>

#### validate\_output

```python
def validate_output(output: t.Any) -> bool
```

Validate the output.

<a id="mopipe.core.segments.outputs.MultivariateSeriesOutput"></a>

## MultivariateSeriesOutput Objects

```python
class MultivariateSeriesOutput(OutputTypeBaseMixin)
```

Mixin class for multivariate series output segments.

<a id="mopipe.core.segments.outputs.MultivariateSeriesOutput.validate_output"></a>

#### validate\_output

```python
def validate_output(output: t.Any) -> bool
```

Validate the output.

<a id="mopipe.core.segments.outputs.SingleValueOutput"></a>

## SingleValueOutput Objects

```python
class SingleValueOutput(OutputTypeBaseMixin)
```

Mixin class for single value output segments.

<a id="mopipe.core.segments.outputs.SingleValueOutput.validate_output"></a>

#### validate\_output

```python
def validate_output(output: t.Any) -> bool
```

Validate the output.

<a id="mopipe.core.segments.outputs.MultiValueOutput"></a>

## MultiValueOutput Objects

```python
class MultiValueOutput(OutputTypeBaseMixin)
```

Mixin class for multiple values output segments.

<a id="mopipe.core.segments.outputs.MultiValueOutput.validate_output"></a>

#### validate\_output

```python
def validate_output(output: t.Any) -> bool
```

Validate the output.

<a id="mopipe.core.segments.outputs.SingleNumericValueOutput"></a>

## SingleNumericValueOutput Objects

```python
class SingleNumericValueOutput(OutputTypeBaseMixin)
```

Mixin class for single numeric value output segments.

<a id="mopipe.core.segments.outputs.SingleNumericValueOutput.validate_output"></a>

#### validate\_output

```python
def validate_output(output: t.Any) -> bool
```

Validate the output.

<a id="mopipe.core.segments.outputs.AnySeriesOutput"></a>

## AnySeriesOutput Objects

```python
class AnySeriesOutput(OutputTypeBaseMixin)
```

Mixin class for any series output segments.

<a id="mopipe.core.segments.outputs.AnySeriesOutput.validate_output"></a>

#### validate\_output

```python
def validate_output(output: t.Any) -> bool
```

Validate the output.

<a id="mopipe.core.segments.outputs.AnyNumericOutput"></a>

## AnyNumericOutput Objects

```python
class AnyNumericOutput(OutputTypeBaseMixin)
```

Mixin class for any numeric output segments.

<a id="mopipe.core.segments.outputs.AnyNumericOutput.validate_output"></a>

#### validate\_output

```python
def validate_output(output: t.Any) -> bool
```

Validate the output.

<a id="mopipe.core.segments.outputs.AnyOutput"></a>

## AnyOutput Objects

```python
class AnyOutput(OutputTypeBaseMixin)
```

Mixin class for any output segments.

<a id="mopipe.core.segments.outputs.AnyOutput.validate_output"></a>

#### validate\_output

```python
def validate_output(output: t.Any) -> bool
```

Validate the output.

<a id="mopipe.core.segments.outputs.OtherOutput"></a>

## OtherOutput Objects

```python
class OtherOutput(OutputTypeBaseMixin)
```

Mixin class for other output segments.

<a id="mopipe.core.segments.outputs.OtherOutput.validate_output"></a>

#### validate\_output

```python
def validate_output(output: t.Any) -> bool
```

Validate the output.

